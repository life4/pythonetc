from __future__ import annotations
from datetime import date
from functools import cached_property
from importlib import import_module
import json
from pathlib import Path
import attr
import yaml
import jsonschema
from markdown_it import MarkdownIt
from .pep import get_pep, PEP

md_parser = MarkdownIt()
SCHEMA_PATH = Path(__file__).parent / 'schema.json'
SCHEMA = json.loads(SCHEMA_PATH.read_text())


def wrap_list(x: object) -> list:
    if isinstance(x, list):
        return x
    return [x]


@attr.s(auto_attribs=True, frozen=True)
class Post:
    path: Path
    markdown: str
    author: str
    id: int | None = None
    qname: list[str] = attr.ib(factory=list, converter=wrap_list)
    pep: int | None = None
    topics: list[str] = attr.ib(factory=list, converter=wrap_list)
    published: date | None = None
    python: str | None = None

    @classmethod
    def from_path(cls, path: Path) -> Post:
        yaml_str, markdown = path.read_text('utf8').lstrip().split('\n---', 1)
        meta: dict = yaml.safe_load(yaml_str)
        qname = meta.setdefault('qname', [])
        if isinstance(meta['qname'], str):
            meta['qname'] = [qname]
        try:
            jsonschema.validate(meta, SCHEMA)
        except jsonschema.ValidationError:
            raise ValueError(f'invalid metadata for {path.name}')
        return cls(**meta, path=path, markdown=markdown)

    @cached_property
    def title(self) -> str:
        first_line = self.markdown.lstrip().split('\n', maxsplit=1)[0]
        return first_line.removeprefix('# ')

    @cached_property
    def md_content(self) -> str:
        return self.markdown.lstrip().split('\n', maxsplit=1)[-1]

    @cached_property
    def html_content(self) -> str:
        return md_parser.render(self.md_content)

    @property
    def slug(self) -> str:
        return self.path.stem

    @cached_property
    def pep_info(self) -> PEP | None:
        if self.pep is None:
            return None
        pep = get_pep(self.pep)
        pep.posts.append(self)
        return pep

    @cached_property
    def module_name(self) -> str | None:
        module_name = self.qname[0]
        while True:
            try:
                import_module(module_name)
            except ImportError:
                if '.' not in module_name:
                    return None
                module_name = module_name.rsplit('.', maxsplit=1)[0]
            else:
                return module_name

    @cached_property
    def telegram_markdown(self) -> str:
        import pandoc.types

        doc = pandoc.read(self.markdown, format='markdown')
        for elt in pandoc.iter(doc):
            if isinstance(elt, pandoc.types.CodeBlock):
                elt[0] = (elt[0][0], [''], elt[0][2])

        return pandoc.write(doc)
