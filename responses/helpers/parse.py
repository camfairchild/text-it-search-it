import re, justext

def remove_html_tags(data: str) -> str:
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def just_the_text(page: str) -> str:
    paragraphs = justext.justext(page, justext.get_stoplist("English"))
    text = "\n".join(p['text'] for p in paragraphs if p['class'] == 'good')
    return text