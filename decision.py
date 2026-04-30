def final_decision(cnn, ocr, sig, wm):
    score = (
        0.4 * cnn +
        0.2 * ocr +
        0.2 * sig +
        0.2 * wm
    )

    if score > 0.75:
        return "REAL", score
    elif score < 0.45:
        return "FAKE", score
    else:
        return "UNCERTAIN", score