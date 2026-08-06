import qrcode

# Social media profile URLs (jahan viral reels/posts hain)
links = {
    "qr-instagram": "https://www.instagram.com/adv.kaptansingh",
    "qr-facebook":  "https://www.facebook.com/adv.KaptanSingh1",
    "qr-twitter":   "https://twitter.com/adv.KaptanSingh",
}

for name, url in links.items():
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    # BJP saffron color QR on white
    img = qr.make_image(fill_color="#c1121f", back_color="white")
    out = f"{name}.png"
    img.save(out)
    print("Saved:", out, "->", url)
