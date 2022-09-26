def main(ctx):
    return dict(
        kind="pipeline",
        type="docker",
        name="default",
        trigger=dict(
            branch="master",
        ),
        steps=[
            dict(
                name="install task",
                image="alpine:latest",
                commands=[
                    "apk add --no-cache wget",
                    "wget https://taskfile.dev/install.sh",
                    "sh install.sh -- latest",
                    "rm install.sh",
                ],
            ),
            dict(
                name="markdownlint",
                image="davidanson/markdownlint-cli2:latest",
                depends_on=["clone"],
                commands=["markdownlint-cli2 '**/*.md'"],
            ),
            step("pytest"),
            step("flake8"),
            step("mypy"),
        ],
    )


def step(task):
    return dict(
        name=task,
        image="python:3.8-buster",
        depends_on=["install task"],
        commands=["./bin/task PYTHON=python3 -f {task}".format(task=task)],
    )
