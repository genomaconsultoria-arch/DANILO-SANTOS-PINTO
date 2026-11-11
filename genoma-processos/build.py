"""Gera index.html (arquivo único) a partir de src/app.html, embutindo os logos Genoma."""
import base64, pathlib
raiz = pathlib.Path(__file__).parent
b64 = lambda n: base64.b64encode((raiz / "assets" / n).read_bytes()).decode()
html = (raiz / "src" / "app.html").read_text(encoding="utf-8")
html = html.replace("__LOGO_H__", b64("logo-genoma-horizontal.webp")).replace("__LOGO_MARK__", b64("logo-genoma-simbolo.webp"))
(raiz / "index.html").write_text(html, encoding="utf-8")
print("index.html gerado:", len(html) // 1024, "KB")
