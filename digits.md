We used to use Arabic digits to record numbers. However, there are many more numeral systems: Chinese (and Suzhou), Chakma, Persian, Hebrew, and so on. And Python supports them when detecting numbers:

```python
int('٤٢')
# 42

'٤٢'.isdigit()
# True

import re
re.compile('\d+').match('٤٢')
# <re.Match object; span=(0, 2), match='٤٢'>
```

If you want to match only Arabic numerals, make an explicit check for it:

```python
n = '٤٢'
n.isdigit() and n.isascii()
# False

re.compile('[0-9]+').match(n)
# None
```

Let's make the full list of supported numerals:

```python
from collections import defaultdict
nums = defaultdict(str)
for i in range(0x110000):
    try:
        int(chr(i))
    except:
        pass
    else:
        nums[int(chr(i))] += chr(i)
dict(nums)
```

```python
{
 0: '0٠۰߀०০੦૦୦௦౦೦൦෦๐໐༠၀႐០᠐᥆᧐᪀᪐᭐᮰᱀᱐꘠꣐꤀꧐꧰꩐꯰０𐒠𐴰𑁦𑃰𑄶𑇐𑋰𑑐𑓐𑙐𑛀𑜰𑣠𑱐𑵐𑶠𖩠𖭐𝟎𝟘𝟢𝟬𝟶𞥐',
 1: '1١۱߁१১੧૧୧௧౧೧൧෧๑໑༡၁႑១᠑᥇᧑᪁᪑᭑᮱᱁᱑꘡꣑꤁꧑꧱꩑꯱１𐒡𐴱𑁧𑃱𑄷𑇑𑋱𑑑𑓑𑙑𑛁𑜱𑣡𑱑𑵑𑶡𖩡𖭑𝟏𝟙𝟣𝟭𝟷𞥑',
 2: '2٢۲߂२২੨૨୨௨౨೨൨෨๒໒༢၂႒២᠒᥈᧒᪂᪒᭒᮲᱂᱒꘢꣒꤂꧒꧲꩒꯲２𐒢𐴲𑁨𑃲𑄸𑇒𑋲𑑒𑓒𑙒𑛂𑜲𑣢𑱒𑵒𑶢𖩢𖭒𝟐𝟚𝟤𝟮𝟸𞥒',
 3: '3٣۳߃३৩੩૩୩௩౩೩൩෩๓໓༣၃႓៣᠓᥉᧓᪃᪓᭓᮳᱃᱓꘣꣓꤃꧓꧳꩓꯳３𐒣𐴳𑁩𑃳𑄹𑇓𑋳𑑓𑓓𑙓𑛃𑜳𑣣𑱓𑵓𑶣𖩣𖭓𝟑𝟛𝟥𝟯𝟹𞥓',
 4: '4٤۴߄४৪੪૪୪௪౪೪൪෪๔໔༤၄႔៤᠔᥊᧔᪄᪔᭔᮴᱄᱔꘤꣔꤄꧔꧴꩔꯴４𐒤𐴴𑁪𑃴𑄺𑇔𑋴𑑔𑓔𑙔𑛄𑜴𑣤𑱔𑵔𑶤𖩤𖭔𝟒𝟜𝟦𝟰𝟺𞥔',
 5: '5٥۵߅५৫੫૫୫௫౫೫൫෫๕໕༥၅႕៥᠕᥋᧕᪅᪕᭕᮵᱅᱕꘥꣕꤅꧕꧵꩕꯵５𐒥𐴵𑁫𑃵𑄻𑇕𑋵𑑕𑓕𑙕𑛅𑜵𑣥𑱕𑵕𑶥𖩥𖭕𝟓𝟝𝟧𝟱𝟻𞥕',
 6: '6٦۶߆६৬੬૬୬௬౬೬൬෬๖໖༦၆႖៦᠖᥌᧖᪆᪖᭖᮶᱆᱖꘦꣖꤆꧖꧶꩖꯶６𐒦𐴶𑁬𑃶𑄼𑇖𑋶𑑖𑓖𑙖𑛆𑜶𑣦𑱖𑵖𑶦𖩦𖭖𝟔𝟞𝟨𝟲𝟼𞥖',
 7: '7٧۷߇७৭੭૭୭௭౭೭൭෭๗໗༧၇႗៧᠗᥍᧗᪇᪗᭗᮷᱇᱗꘧꣗꤇꧗꧷꩗꯷７𐒧𐴷𑁭𑃷𑄽𑇗𑋷𑑗𑓗𑙗𑛇𑜷𑣧𑱗𑵗𑶧𖩧𖭗𝟕𝟟𝟩𝟳𝟽𞥗',
 8: '8٨۸߈८৮੮૮୮௮౮೮൮෮๘໘༨၈႘៨᠘᥎᧘᪈᪘᭘᮸᱈᱘꘨꣘꤈꧘꧸꩘꯸８𐒨𐴸𑁮𑃸𑄾𑇘𑋸𑑘𑓘𑙘𑛈𑜸𑣨𑱘𑵘𑶨𖩨𖭘𝟖𝟠𝟪𝟴𝟾𞥘',
 9: '9٩۹߉९৯੯૯୯௯౯೯൯෯๙໙༩၉႙៩᠙᥏᧙᪉᪙᭙᮹᱉᱙꘩꣙꤉꧙꧹꩙꯹９𐒩𐴹𑁯𑃹𑄿𑇙𑋹𑑙𑓙𑙙𑛉𑜹𑣩𑱙𑵙𑶩𖩩𖭙𝟗𝟡𝟫𝟵𝟿𞥙',
}
```
