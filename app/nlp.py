import spacy

# Modeli yüklə
try:
    nlp = spacy.load("en_core_web_sm")  # Modelin düzgün yükləndiyini yoxla
except Exception as e:
    print("NLP modeli yüklənmədi:", e)

# NLP üçün cavab qaytarma funksiyası
def get_response(message: str):
    message = message.lower().strip()  # Mesajı kiçik hərflərə çevir və boşluqları sil
    
    if "kurslar" in message or "təlimlər" in message:
        return "Baku Design Center-də müxtəlif kurslar təklif olunur: Qrafik dizayn, UX/UI dizayn, Proqramlaşdırma və s. Ətraflı məlumat üçün rəsmi saytımıza baxın."
    elif "qeydiyyat" in message or "necə yazılım?" in message:
        return "Kurslara qeydiyyat üçün veb saytımıza daxil olun və müraciət formasını doldurun."
    elif "əlaqə" in message or "contact" in message:
        return "Baku Design Center ilə əlaqə saxlamaq üçün +994 55 253 00 30 nömrəsinə zəng edə və ya email göndərə bilərsiniz."
    elif "salam" in message or "hello" in message:
        return "Salam! Mən Baku Design Center-in virtual asistentiyəm. Sizə necə kömək edə bilərəm?"
    else:
        return "Bağışlayın, sualınızı başa düşmədim. Zəhmət olmasa, daha dəqiq ifadə edin."
