import pdfrw
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from faker import Faker
import random


def reverse_hebrew_text(text):
    words = text.split()
    for index, item in enumerate(words):
        if not item.isdigit():  # Check if the item is a word (all alphabetic)
            words[index] = item[::-1]  # Reverse the word

    # Reverse the list of words
    words.reverse()
    sentence = " ".join(words)

    # Join the words back together with spaces, preserving the original word order
    return sentence


misradim = [
    "פקיד שומה טבריה",
    "פקיד שומה עפולה",
    "מע''מ טבריה",
    "פקיד שומה צפת",
    "פקיד שומה נצרת",
    "מע''מ נוף הגליל",
    "פקיד שומה עכו",
    "מע''מ עכו",
    "יחידה ארצית לבלו ומס קניה",
    "פקיד שומה חיפה",
    "מע''מ חיפה",
    "מכס חיפה",
    "מיסוי מקרקעין ירושלים",
    "מע''מ חדרה",
    "פקיד שומה חדרה",
    "מע''מ תל אביב 1",
    "מע''מ תל אביב 2",
    "פקיד שומה נתניה",
    "מע''מ נתניה",
    "פקיד שומה כפר סבא",
    "פקיד שומה פתח תקוה",
    "פקיד שומה רמלה",
    "פקיד שומה רחובות",
    "מע''מ רחובות",
    "מע'מ פתח תקווה",
    "מיסוי מקרקעין מרכז",
    "פקיד שומה תל אביב 5",
    "פקיד שומה תל אביב1",
    "פקיד שומה חולון",
    "פקיד שומה תל אביב 4",
    "מע''מ גוש דן",
    "מע''מ תל אביב 3",
    "פקיד שומה למפעלים גדולים",
    "פקיד שומה תל אביב 3",
    "פקיד שומה גוש דן",
    "מיסוי מקרקעין חיפה",
    "פקיד שומה ירושלים 1",
    'מע"מ ומכס ירושלים',
    "פקיד שומה ירושלים 3",
    "מכס מרכז",
    'מע"מ תל אביב מרכז',
    "מכס נתב''ג",
    "מכס אשדוד",
    "מע''מ אשדוד",
    "מע''מ באר שבע",
    "מיסוי מקרקעין תל אביב",
    "פקיד שומה אשקלון",
    "פקיד שומה באר שבע",
    "פקיד שומה חקירות תל אביב",
    "פקיד שומה חקירות חיפה וצפון",
    "פקיד שומה חקירות ירושלים ודרום",
    "פקיד שומה חקירות מרכז",
    "הוצאה לפועל תל אביב והמרכז",
    "הוצאה לפועל חיפה והצפון",
    "הוצאה לפועל ירושלים והדרום",
    "חקירות מע'מ חיפה",
    "חקירות מע''מ תל אביב",
    "חקירות מע''מ באר שבע",
    "חקירות מע''מ ירושלים",
    "יחידה ארצית לחשיפת יעדים",
    "מיסוי מקרקעין  חדרה",
    "הוצל'פ באר שבע",
    "מיסוי מקרקעין טבריה",
    "יחידה ארצית למאבק בפשיעה",
    "רשות המסים בישראל אזור השרון",
    "מיסוי מקרקעין נצרת",
    "מיסוי מקרקעין נתניה",
    "יחידות מש~מ -מידע שירות ומשאבים מס הכנסה לפרטים הקש כפתור חץ",
    "הנהלת רשות המסים ת~א",
    "פקיד שומה ירושלים 2",
    "מיסוי מקרקעין רחובות",
    "פקיד שומה אילת",
    "מכס אילת",
    "מכס ניצנה",
    "בית מכס נהר הירדן",
    "מכס גשר אלנבי",
    "מיסוי מקרקעין באר שבע",
    "אולם נוסעים נתב''ג",
    "מעברי גבול",
    "מע''מ רמלה",
    "מוקד מידע  רשות המסים",
    "הנהלת רשות המסים מס הכנסה (בית דניאל)",
    "יחידה משפטית",
    "הנהלת רשות המסים מכס ומע''מ",
    "הנהלת רשות המסים מס הכנסה ירושלים",
    "ביקורת פנים- הנהלת הרשות",
    "מקצועית - הנהלת הרשות",
    "ייעוץ משפטי- הנהלת הרשות",
    "הון אנושי- הנהלת הרשות",
    "רכש נכסים ולוג~- הנהלת הרשות",
    "חשבות - הנהלת הרשות",
    "אכיפה וגביה - הנהלת הרשות",
    "שומה וביקורת - הנהלת הרשות",
    "תכנון וכלכלה",
    "חקירות ומודיעין- הנהלת הרשות",
    "שירות לקוחות- הנהלת הרשות",
    "הנהלת מס הכנסה- הנהלת הרשות",
    "הנהלת מיסוי מקרקעין- הנהלת הרשות",
]

transactions_description = [
    "שירותי ייעוץ עסקי - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    "ריהוט חדש למשרדי החברה - הוצאה בתחום הפעילות של  נכסים מוחשיים.",
    "פרויקט בנייה - הכנסה בתחום הפעילות של מתן שירותים מקצועיים.",
    "תשלום לספקים עבור חומרי גלם - הוצאה בתחום הפעילות של רכש והפצה.",
    "עבודה לעובדים בפרויקט - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    "מענק ממשלתי עבור מחקר ופיתוח - הכנסה בתחום הפעילות של מחקר ופיתוח.",
    "פרסום ושיווק בקמפיין חדש - הוצאה בתחום הפעילות של שיווק ופרסום.",
    "השכרת משרדים לשנה הקרובה - הוצאה בתחום הפעילות של ניהול תפעולי.",
    "רכב חדש לצורכי החברה - הוצאה בתחום הפעילות של  נכסים מוחשיים.",
    "שירותי אבטחת מידע - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    "מכירת מכונה ישנה - הכנסה בתחום הפעילות של מכירת נכסים מוחשיים.",
    "החזר מס בעקבות תשלום יתר - הכנסה בתחום הפעילות של ניהול פיננסי.",
    "שירותי תרגום מסמכים - הוצאה בתחום הפעילות של מתן שירותים מקצועיים.",
    "השקעה במחקר שוק לפיתוח מוצרים - הוצאה בתחום הפעילות של מחקר ופיתוח.",
    " פרויקט עתידי - הכנסה בתחום הפעילות של מתן שירותים.",
    " שירותי יחסי ציבור - הוצאה בתחום הפעילות של שיווק ופרסום.",
    " מערכת מחשוב מתקדמת - הוצאה בתחום הפעילות של  נכסים מוחשיים.",
    "שירותי ניהול פרויקטים - הכנסה בתחום הפעילות של מתן שירותים מקצועיים.",
    "הוצאות תפעול למפעל - הוצאה בתחום הפעילות של ניהול תפעולי.",
    "כנסים והדרכות מקצועיות - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    "שטח לפרויקט עתידי - הוצאה בתחום הפעילות של  נכסים מוחשיים.",
    "השקעה בתוכנה לניהול לקוחות - הוצאה בתחום הפעילות של ניהול תפעולי.",
    " שירותי ייעוץ משפטי - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    "הספקת שירותי אבטחה - הכנסה בתחום הפעילות של מתן שירותים מקצועיים.",
    "אחזקת בניינים ומתקנים - הוצאה בתחום הפעילות של ניהול תפעולי.",
    "השקעה בקמפיין שיווק בינלאומי - הוצאה בתחום הפעילות של שיווק ופרסום.",
    " שירותי גרפיקה ועיצוב - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    ' כרטיסים לכנס מקצועי בחו"ל - הוצאה בתחום הפעילות של ניהול משאבי אנוש.',
    "קבלת פיצוי מחברת ביטוח - הכנסה בתחום הפעילות של ניהול פיננסי.",
    "החזרי מס בעקבות דיווח עודף - הכנסה בתחום הפעילות של ניהול פיננסי.",
    " זכויות למאמרים - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    " הוצאות ארנונה וחשמל - הוצאה בתחום הפעילות של ניהול תפעולי.",
    " שירותי כתיבת תוכן - הכנסה בתחום הפעילות של מתן שירותים מקצועיים.",
    "השקעה במערכת אבטחה חדשה למפעל - הוצאה בתחום הפעילות של  נכסים מוחשיים.",
    "עבור שירותי אחסון אתרים - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    " מלאי חדש לחנות - הוצאה בתחום הפעילות של  נכסים מוחשיים.",
    "הוצאות על אירועים לעובדים - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    "עבור שירותי רואי חשבון - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    "קבלת דיבידנדים מהשקעות - הכנסה בתחום הפעילות של ניהול פיננסי.",
    "השקעה במחקר טכנולוגי חדש - הוצאה בתחום הפעילות של מחקר ופיתוח.",
    "עבור שירותי בדיקה והערכה - הכנסה בתחום הפעילות של מתן שירותים מקצועיים.",
    " מערכת חימום חדשה למשרדים - הוצאה בתחום הפעילות של  נכסים מוחשיים.",
    "עבור קורסים מקצועיים לעובדים - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    "השקעה בהקמת קו ייצור חדש - הוצאה בתחום הפעילות של ייצור ותפעול.",
    "קבלת החזר הוצאות על נסיעות - הכנסה בתחום הפעילות של ניהול פיננסי.",
    " רישום פטנטים - הוצאה בתחום הפעילות של מחקר ופיתוח.",
    "הוצאות על פרסום ברשתות חברתיות - הוצאה בתחום הפעילות של שיווק ופרסום.",
    "עבור שירותי ניקיון למשרדים - הוצאה בתחום הפעילות של ניהול תפעולי.",
    " ביטוח לכלי רכב של החברה - הוצאה בתחום הפעילות של ניהול פיננסי.",
    "תשלום על שירותי הדרכה - הכנסה בתחום הפעילות של מתן שירותים מקצועיים.",
    "השקעה בפיתוח מוצר חדש - הוצאה בתחום הפעילות של מחקר ופיתוח.",
    " רישוי תוכנות - הוצאה בתחום הפעילות של ניהול תפעולי.",
    "החזר מספק בעקבות קנייה כושלת - הכנסה בתחום הפעילות של ניהול פיננסי.",
    " חומרים לפרויקט בנייה - הוצאה בתחום הפעילות של ייצור ותפעול.",
    " שירותי צילום מקצועי - הוצאה בתחום הפעילות של שיווק ופרסום.",
    "קבלת מענק מחקר מאוניברסיטה - הכנסה בתחום הפעילות של מחקר ופיתוח.",
    "השקעה במערכת ניהול עובדים - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    "תשלום לספקי תקשורת ואינטרנט - הוצאה בתחום הפעילות של ניהול תפעולי.",
    "על מכירת נכס דיגיטלי - הכנסה בתחום הפעילות של מכירת נכסים לא מוחשיים.",
    "עיצוב פנים למשרדי החברה - הוצאה בתחום הפעילות של  נכסים מוחשיים.",
    " שירותי עורך דין - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    "הוצאות על תחזוקת מערכות מחשוב - הוצאה בתחום הפעילות של ניהול תפעולי.",
    " מכשירי כושר לעובדים - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    "תשלום על קידום אתרים בגוגל - הוצאה בתחום הפעילות של שיווק ופרסום.",
    "קבלת פיצויים מבית המשפט - הכנסה בתחום הפעילות של ניהול פיננסי.",
    "הוצאות על מסיבת חברה שנתית - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    "השקעה בתשתיות לוגיסטיות חדשות - הוצאה בתחום הפעילות של ניהול תפעולי.",
    " רישוי תוכנה - הכנסה בתחום הפעילות של מכירת נכסים לא מוחשיים.",
    " מכונת דפוס חדשה - הוצאה בתחום הפעילות של  נכסים מוחשיים.",
    "על כרטיסי טיסה לפגישות עסקיות - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    "השקעה בתוכנת הגנה מפני סייבר - הוצאה בתחום הפעילות של ניהול תפעולי.",
    "תשלום לספקים עבור מזון לכנסים - הוצאה בתחום הפעילות של ניהול תפעולי.",
    "הוצאות על פרסום ברדיו ובטלוויזיה - הוצאה בתחום הפעילות של שיווק ופרסום.",
    " מניות בחברת סטארטאפ - הוצאה בתחום הפעילות של ניהול פיננסי.",
    "תשלום על שירותי תמיכה טכנית - הכנסה בתחום הפעילות של מתן שירותים מקצועיים.",
    "השקעה בבניית מרכז לוגיסטי חדש - הוצאה בתחום הפעילות של ניהול תפעולי.",
    "תשלום על שירותי רווחת עובדים - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    " דומיין ואתר אינטרנט - הוצאה בתחום הפעילות של ניהול תפעולי.",
    "החזר תשלום בעקבות טעות חשבונאית - הכנסה בתחום הפעילות של ניהול פיננסי.",
    "השקעה בשיפוץ מפעלי הייצור - הוצאה בתחום הפעילות של ייצור ותפעול.",
    " קמפיין פרסום במגזין מקצועי - הוצאה בתחום הפעילות של שיווק ופרסום.",
    "קבלת תשלום על שירותי הנדסה - הכנסה בתחום הפעילות של מתן שירותים מקצועיים.",
    "השקעה במערכת CRM לניהול לקוחות - הוצאה בתחום הפעילות של ניהול תפעולי.",
    " הדרכות ניהוליות לעובדים - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    " חבילות תמיכה טכנולוגית - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    "החזר הוצאות מספק שירותים - הכנסה בתחום הפעילות של ניהול פיננסי.",
    "השקעה בפרויקט מחקרי משותף - הוצאה בתחום הפעילות של מחקר ופיתוח.",
    "תשלום על הובלה ואחסון של סחורות - הוצאה בתחום הפעילות של רכש והפצה.",
    "תשלום על ייעוץ בהנדסה אזרחית - הכנסה בתחום הפעילות של מתן שירותים.",
    "השקעה במערכת בקרה ואוטומציה - הוצאה בתחום הפעילות של ייצור ותפעול.",
    "תשלום על פיתוח אתר לחברה - הוצאה בתחום הפעילות של שיווק ופרסום.",
    "קבלת מענק על פיתוח פתרונות סביבתיים - הכנסה בתחום הפעילות של מחקר ופיתוח.",
    "השקעה בשדרוג מערכות טכנולוגיות - הוצאה בתחום הפעילות של ניהול תפעולי.",
    " חקר שוק ובדיקות כדאיות - הוצאה בתחום הפעילות של שיווק ופרסום.",
    "קבלת תשלום על הדרכות תוכנה - הכנסה בתחום הפעילות של מתן שירותים מקצועיים.",
    "הוצאות על ציוד מגן לעובדי המפעל - הוצאה בתחום הפעילות של ניהול משאבי אנוש.",
    " טיפול משפטי בתביעות - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    "השקעה בקניית שטח חקלאי לעתיד - הוצאה בתחום הפעילות של  נכסים מוחשיים.",
    "קבלת תשלום על פרסום בחסות החברה - הכנסה בתחום הפעילות של שיווק ופרסום.",
    "השקעה בתשתיות פיתוח בסביבת ענן - הוצאה בתחום הפעילות של ניהול תפעולי.",
    "תשלום לספקי שירותים טכנולוגיים - הוצאה בתחום הפעילות של ייעוץ ומתן שירותים.",
    "קבלת פיצוי על הפסד מיזמים - הכנסה בתחום הפעילות של ניהול פיננסי.",
]

shitot = [
    "שיטת השוואת המחיר - השוואה בין המחיר שנקבע לבין המחיר שנקבע בעסקה דומה",
    "שיטה המשווה את שיעור הרווחיות - השוואה בין שיעור הרווחיות בעסקה לבין שיעור הרווחיות",
    "שיטת חלוקת הרווח או ההפסד",
    "שיטה אחרת",
]

jobs = [
    "מנהל פרויקט",
    "מתכנת",
    "מהנדס",
    "מעצב גרפי",
    "כותב תוכן",
    "עורך דין",
    "רופא",
    "שף",
    "צלם",
    "נגר",
    "רוקח",
    "שרברב",
    "נהג",
    "אדריכל",
    "מזכיר",
    "מורה",
    "גנן",
    "חקלאי",
    "עורך וידאו",
    "ספרן",
    "צלם וידאו",
    "מאבטח",
    "סוכן מכירות",
    "שיפוצניק",
    'מנכ"ל',
    "מנהל חשבונות",
    "מדען",
    "חוקר פרטי",
    "מוזיקאי",
    "אח",
    "רופא שיניים",
    "מורה פרטי",
    "יועץ עסקי",
    "מאמן כושר",
    "חשמלאי",
    "מומחה SEO",
    "קופירייטר",
    "מעצב פנים",
    "טכנאי מחשבים",
    "אומן",
    "מדריך טיולים",
    "מורה ליוגה",
    "מתווך",
    "מפיק אירועים",
    "שוחט",
    "בשלן",
    "שרטט",
    "כלבן",
    "מודד",
    "מסגר",
]


def random_misrad():
    random_index = random.randint(1, 98) - 1
    return misradim[random_index]


def random_job():
    random_index = random.randint(1, 50) - 1
    return jobs[random_index]


def random_transaction_desc():
    random_index = random.randint(1, 100) - 1
    return transactions_description[random_index]


def random_shita():
    random_index = random.randint(1, 4) - 1
    return shitot[random_index]


# Initialize the Faker object with Hebrew locale
fake = Faker("he_IL")
fake_english = Faker("en_US")

pdfmetrics.registerFont(TTFont("David", "David.ttf"))

# Input and output file paths
template_pdf_path = "./Service_Pages_Income_tax_itc1385.pdf"


def create_overlay_pdf(field_values, overlay_path):
    c = canvas.Canvas(overlay_path, pagesize=letter)
    # Customize coordinates and font settings as needed
    c.setFont("Helvetica", 10)
    c.drawString(200, 725, field_values.get("שנה", ""))
    c.drawString(230, 675, field_values.get("מספר תיק במס הכנסה", ""))
    c.drawString(134, 675, field_values.get("מספר תיק ניכויים", ""))
    c.drawString(65, 675, field_values.get("מספר טלפון", ""))
    c.setFont("David", 11)  # Set font to 'David' with size 12
    c.drawString(400, 675, reverse_hebrew_text(field_values.get("שם הנישום")))
    c.drawString(350, 650, reverse_hebrew_text(field_values.get("כתובת העסק")))
    c.setFont("David", 9)  # Set font to 'David' with size 12
    c.drawString(152, 650, reverse_hebrew_text(field_values.get("משרד פקיד השומה")))
    c.drawString(
        35, 650, reverse_hebrew_text(field_values.get("משרד פקיד השומה ניכויים"))
    )
    c.setFont("David", 11)  # Set font to 'David' with size 12
    c.drawString(430, 600, field_values.get("שם הצד הקשור"))
    c.drawString(280, 600, field_values.get('(TIN) מספר זיהוי לצרכי מס בחו"ל'))
    c.drawString(80, 600, reverse_hebrew_text(field_values.get("כתובת")))
    c.setFont("David", 12)  # Set font to 'David' with size 12
    c.drawString(280, 560, reverse_hebrew_text(field_values.get("מספר העסקה")))
    c.setFont("David", 11)  # Set font to 'David' with size 12
    c.drawString(33, 540, reverse_hebrew_text(field_values.get("1תיאור העסקה")))
    c.drawString(33, 520, reverse_hebrew_text(field_values.get("2תיאור העסקה")))
    c.drawString(40, 500, reverse_hebrew_text(field_values.get("1השיטה שננקטה")))
    c.drawString(40, 480, reverse_hebrew_text(field_values.get("2השיטה שננקטה")))
    c.setFont("David", 12)  # Set font to 'David' with size 12
    c.drawString(200, 460, reverse_hebrew_text(field_values.get("1שיעור הרווחיות")))
    c.drawString(200, 440, reverse_hebrew_text(field_values.get("2שיעור הרווחיות")))
    c.drawString(200, 420, reverse_hebrew_text(field_values.get("סכום העסקה")))
    c.setFont("David", 11)  # Set font to 'David' with size 12
    c.drawString(95 if random.choice([True, False]) else 130, 380, "x")
    c.drawString(95 if random.choice([True, False]) else 130, 356, "x")
    c.drawString(95 if random.choice([True, False]) else 130, 334, "x")
    c.drawString(95 if random.choice([True, False]) else 130, 313, "x")
    c.drawString(95 if random.choice([True, False]) else 130, 292, "x")
    c.setFont("David", 12)  # Set font to 'David' with size 12
    c.drawString(450, 190, field_values.get("תאריך", ""))
    c.drawString(330, 190, reverse_hebrew_text(field_values.get("שם")))
    c.drawString(165, 190, field_values.get("תפקיד"))
    c.drawString(70, 190, reverse_hebrew_text(field_values.get("חתימה")))
    c.save()


def merge_pdfs(template_path, overlay_path, output_path):
    template_pdf = pdfrw.PdfReader(template_path)
    overlay_pdf = pdfrw.PdfReader(overlay_path)
    for page, overlay_page in zip(template_pdf.pages, overlay_pdf.pages):
        merger = pdfrw.PageMerge(page)
        merger.add(overlay_page).render()
    pdfrw.PdfWriter(output_path, trailer=template_pdf).write()


def get_job_under_22_chars():
    while True:
        job = fake_english.job()
        if len(job) <= 22:
            return job


def get_company_under_22_chars():
    while True:
        company = fake_english.company()
        if len(company) <= 22:
            return company


def generate_pdfs():
    for i in range(1, 2):
        name = fake.name()
        map_item = {
            "שנה": str(fake.year()),
            "שם הנישום": name,
            "מספר תיק במס הכנסה": "  ".join(
                str(fake.random_number(digits=9, fix_len=True))
            ),
            "מספר תיק ניכויים": "  ".join(
                str(fake.random_number(digits=8, fix_len=True))
            ),
            "מספר טלפון": fake.phone_number(),
            "כתובת העסק": fake.address(),
            "משרד פקיד השומה": random_misrad(),
            "משרד פקיד השומה ניכויים": random_misrad(),
            "שם הצד הקשור": get_company_under_22_chars(),
            '(TIN) מספר זיהוי לצרכי מס בחו"ל': " ".join(
                str(fake.random_number(digits=9, fix_len=True))
            ),
            "כתובת": fake.address(),
            "מספר העסקה": " ".join(str(fake.random_number(digits=8, fix_len=True))),
            "1תיאור העסקה": random_transaction_desc(),
            "2תיאור העסקה": random_transaction_desc(),
            "1השיטה שננקטה": random_shita(),
            "2השיטה שננקטה": random_shita(),
            "1שיעור הרווחיות": str(fake.random_int(min=10000, max=100000)),
            "2שיעור הרווחיות": str(fake.random_int(min=10000, max=100000)),
            "סכום העסקה": str(fake.random_int(min=50000, max=200000)),
            "העסקה המדווחת היא עסקה חד פעמית": "x",
            "העסקה מסוג שירותים המוסיפים ערך נמוך": "x",
            "העסקה מסוג שירותי שיווק": "x",
            "העסקה מסוג שירותי הפצה": "x",
            "קיים דיווח חקר תנאי שוק": "x",
            "תאריך": fake.date(pattern="%d/%m/%Y"),
            "שם": name,
            "תפקיד": get_job_under_22_chars(),
            "חתימה": name,
        }
        overlay_pdf_path = f"./overlay_{str(i)}.pdf"
        filled_pdf_path = f"./Filled_Service_Pages_Income_tax_itc1385_{str(i)}.pdf"
        create_overlay_pdf(map_item, overlay_pdf_path)
        merge_pdfs(template_pdf_path, overlay_pdf_path, filled_pdf_path)


generate_pdfs()
