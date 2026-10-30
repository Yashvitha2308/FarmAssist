
from datetime import date

CROP_DATA = {
    "Bengal Gram (Chickpea)": {
        "seasons": ["Rabi"],
        "soils": ["Black", "Red", "Alluvial"],
        "water": ["Limited", "Rainfed", "Available"],
        "temperature": (15, 30),
        "reason": {
            "English": "A Rabi pulse crop suitable for some areas with limited irrigation.",
            "Telugu": "రబీ సీజన్‌లో సాగు చేసే పప్పుధాన్య పంట. తక్కువ నీటి సదుపాయం ఉన్న కొన్ని ప్రాంతాలకు అనుకూలంగా ఉంటుంది.",
            "Hindi": "रबी मौसम की दलहनी फसल, जो कुछ सीमित सिंचाई वाले क्षेत्रों के लिए उपयुक्त हो सकती है।"
        },
        "warning": {
            "English": "Avoid waterlogging and excessive irrigation.",
            "Telugu": "పొలంలో నీరు నిల్వ ఉండకుండా చూడండి. అధికంగా నీరు పెట్టకండి.",
            "Hindi": "खेत में पानी जमा न होने दें और अधिक सिंचाई से बचें।"
        }
    },
    "Mustard": {
        "seasons": ["Rabi"],
        "soils": ["Black", "Alluvial", "Sandy"],
        "water": ["Limited", "Rainfed", "Available"],
        "temperature": (10, 30),
        "reason": {
            "English": "A Rabi oilseed crop that generally requires relatively less water.",
            "Telugu": "రబీ సీజన్‌లో పండించే నూనెగింజల పంట. సాధారణంగా తక్కువ నీరు అవసరం.",
            "Hindi": "रबी मौसम की तिलहन फसल, जिसे सामान्यतः कम पानी की आवश्यकता होती है।"
        },
        "warning": {
            "English": "Check local variety and sowing recommendations.",
            "Telugu": "స్థానికంగా అనుకూలమైన విత్తన రకం, విత్తే సమయం తెలుసుకోండి.",
            "Hindi": "स्थानीय किस्म और बुवाई की सलाह की जाँच करें।"
        }
    },
    "Wheat": {
        "seasons": ["Rabi"],
        "soils": ["Black", "Alluvial"],
        "water": ["Available", "Limited"],
        "temperature": (10, 25),
        "reason": {
            "English": "A Rabi cereal crop suited to cooler wheat-growing regions.",
            "Telugu": "చల్లని వాతావరణం ఉండే గోధుమ సాగు ప్రాంతాల్లో అనుకూలమైన రబీ పంట.",
            "Hindi": "ठंडे गेहूँ उत्पादक क्षेत्रों के लिए उपयुक्त रबी अनाज की फसल।"
        },
        "warning": {
            "English": "Requires suitable temperatures and timely irrigation.",
            "Telugu": "అనుకూలమైన ఉష్ణోగ్రత, సరైన సమయంలో నీటి సరఫరా అవసరం.",
            "Hindi": "उपयुक्त तापमान और समय पर सिंचाई आवश्यक है।"
        }
    },
    "Maize": {
        "seasons": ["Kharif", "Rabi", "Zaid"],
        "soils": ["Black", "Red", "Alluvial"],
        "water": ["Available", "Limited"],
        "temperature": (18, 35),
        "reason": {
            "English": "Can be cultivated in different seasons where local conditions are suitable.",
            "Telugu": "స్థానిక వాతావరణం, నేల పరిస్థితులు అనుకూలంగా ఉంటే వివిధ సీజన్లలో సాగు చేయవచ్చు.",
            "Hindi": "स्थानीय परिस्थितियाँ अनुकूल होने पर इसे अलग-अलग मौसमों में उगाया जा सकता है।"
        },
        "warning": {
            "English": "Needs adequate moisture, especially during flowering.",
            "Telugu": "ముఖ్యంగా పూత దశలో తగినంత తేమ అవసరం.",
            "Hindi": "विशेषकर फूल आने के समय पर्याप्त नमी आवश्यक है।"
        }
    },
    "Groundnut": {
        "seasons": ["Kharif", "Rabi", "Zaid"],
        "soils": ["Red", "Sandy"],
        "water": ["Available", "Limited", "Rainfed"],
        "temperature": (20, 35),
        "reason": {
            "English": "An oilseed crop that can suit light-textured, well-drained soils.",
            "Telugu": "తేలికపాటి నేలలు, నీరు బాగా ఇంకిపోయే భూముల్లో సాగుకు అనుకూలంగా ఉండే నూనెగింజల పంట.",
            "Hindi": "हल्की और अच्छी जल निकासी वाली मिट्टी में उपयुक्त हो सकने वाली तिलहन फसल।"
        },
        "warning": {
            "English": "Avoid waterlogging and maintain moisture during flowering.",
            "Telugu": "పొలంలో నీరు నిల్వ ఉండకూడదు. పూత దశలో నేలలో తేమ ఉండాలి.",
            "Hindi": "जलभराव से बचें और फूल आने के समय मिट्टी में नमी बनाए रखें।"
        }
    },
    "Sorghum (Jowar)": {
        "seasons": ["Kharif", "Rabi"],
        "soils": ["Black", "Red"],
        "water": ["Rainfed", "Limited", "Available"],
        "temperature": (20, 35),
        "reason": {
            "English": "A relatively drought-tolerant cereal crop for suitable dryland regions.",
            "Telugu": "తక్కువ వర్షపాతం ఉండే అనుకూలమైన మెట్ట ప్రాంతాల్లో సాగు చేయగల తృణధాన్య పంట.",
            "Hindi": "उपयुक्त शुष्क क्षेत्रों के लिए अपेक्षाकृत सूखा सहन करने वाली अनाज की फसल।"
        },
        "warning": {
            "English": "Choose a locally recommended variety.",
            "Telugu": "మీ ప్రాంతానికి అనుకూలమైన విత్తన రకాన్ని ఎంచుకోండి.",
            "Hindi": "अपने क्षेत्र के लिए अनुशंसित किस्म चुनें।"
        }
    },
    "Rice (Paddy)": {
        "seasons": ["Kharif", "Rabi"],
        "soils": ["Alluvial", "Black"],
        "water": ["Available"],
        "temperature": (20, 35),
        "reason": {
            "English": "Can suit regions with reliable water supply and suitable field conditions.",
            "Telugu": "తగినంత నీటి సదుపాయం, అనుకూలమైన పొల పరిస్థితులు ఉన్న ప్రాంతాల్లో సాగు చేయవచ్చు.",
            "Hindi": "विश्वसनीय जल आपूर्ति और उपयुक्त खेत की स्थिति वाले क्षेत्रों में उगाया जा सकता है।"
        },
        "warning": {
            "English": "Requires reliable water management.",
            "Telugu": "నీటి సరఫరా, పొలంలో నీటి నిర్వహణ సరిగ్గా ఉండాలి.",
            "Hindi": "उचित जल प्रबंधन आवश्यक है।"
        }
    },
    "Cotton": {
        "seasons": ["Kharif"],
        "soils": ["Black", "Alluvial"],
        "water": ["Rainfed", "Limited", "Available"],
        "temperature": (21, 35),
        "reason": {
            "English": "A major commercial crop in suitable cotton-growing regions.",
            "Telugu": "పత్తి సాగుకు అనుకూలమైన ప్రాంతాల్లో పండించే ప్రధాన వాణిజ్య పంట.",
            "Hindi": "उपयुक्त कपास उत्पादक क्षेत्रों की एक प्रमुख व्यावसायिक फसल।"
        },
        "warning": {
            "English": "Check local sowing dates and pest management requirements.",
            "Telugu": "స్థానిక విత్తే సమయం, చీడపీడల నివారణ చర్యలు తెలుసుకోండి.",
            "Hindi": "स्थानीय बुवाई के समय और कीट प्रबंधन की जानकारी लें।"
        }
    },
    "Soybean": {
        "seasons": ["Kharif"],
        "soils": ["Black", "Alluvial"],
        "water": ["Rainfed", "Limited", "Available"],
        "temperature": (20, 35),
        "reason": {
            "English": "A Kharif oilseed crop grown in suitable monsoon regions.",
            "Telugu": "అనుకూలమైన వర్షాకాల ప్రాంతాల్లో సాగు చేసే ఖరీఫ్ నూనెగింజల పంట.",
            "Hindi": "उपयुक्त मानसूनी क्षेत्रों में उगाई जाने वाली खरीफ तिलहन फसल।"
        },
        "warning": {
            "English": "Avoid prolonged waterlogging.",
            "Telugu": "ఎక్కువసేపు పొలంలో నీరు నిల్వ ఉండకుండా చూడండి.",
            "Hindi": "लंबे समय तक जलभराव से बचें।"
        }
    },
    "Lentil": {
        "seasons": ["Rabi"],
        "soils": ["Black", "Alluvial"],
        "water": ["Limited", "Rainfed"],
        "temperature": (15, 30),
        "reason": {
            "English": "A Rabi pulse crop that can suit cooler regions with limited irrigation.",
            "Telugu": "తక్కువ నీటి సదుపాయం ఉన్న చల్లని ప్రాంతాల్లో సాగుకు అనుకూలంగా ఉండే రబీ పప్పుధాన్య పంట.",
            "Hindi": "सीमित सिंचाई वाले ठंडे क्षेत्रों के लिए उपयुक्त रबी दलहनी फसल।"
        },
        "warning": {
            "English": "Check regional suitability and sowing time.",
            "Telugu": "మీ ప్రాంతానికి అనుకూలత, విత్తే సమయాన్ని తనిఖీ చేయండి.",
            "Hindi": "क्षेत्रीय उपयुक्तता और बुवाई के समय की जाँच करें।"
        }
    }
}


def get_season(month):
    if month in [6, 7, 8, 9]:
        return "Kharif"
    elif month in [10, 11, 12, 1, 2]:
        return "Rabi"
    return "Zaid"


SEASON_TRANSLATIONS = {
    "English": {
        "Kharif": "Kharif",
        "Rabi": "Rabi",
        "Zaid": "Zaid"
    },
    "Telugu": {
        "Kharif": "ఖరీఫ్",
        "Rabi": "రబీ",
        "Zaid": "జైద్"
    },
    "Hindi": {
        "Kharif": "खरीफ",
        "Rabi": "रबी",
        "Zaid": "जायद"
    }
}


def get_crop_recommendations(
    soil,
    irrigation,
    temperature,
    rainfall_mm,
    rainfall_probability,
    month=None,
    language="English"
):
    if month is None:
        month = date.today().month

    if language not in ["English", "Telugu", "Hindi"]:
        language = "English"

    if soil not in ["Red", "Black", "Sandy", "Alluvial", "Unknown"]:
        raise ValueError("Invalid soil type.")

    if irrigation not in ["Available", "Limited", "Rainfed"]:
        raise ValueError("Invalid irrigation selection.")

    if not 0 <= rainfall_probability <= 100:
        raise ValueError("Rainfall probability must be between 0 and 100.")

    if rainfall_mm < 0:
        raise ValueError("Rainfall cannot be negative.")

    season = get_season(month)
    suitable = []
    less_suitable = []

    for crop, details in CROP_DATA.items():
        score = 0
        reasons = []
        concerns = []

        if season in details["seasons"]:
            score += 30
        else:
            concerns.append({
                "English": f"Not a typical {season} crop.",
                "Telugu": f"ఇది సాధారణంగా {SEASON_TRANSLATIONS['Telugu'][season]} సీజన్‌లో పండించే పంట కాదు.",
                "Hindi": f"यह सामान्यतः {SEASON_TRANSLATIONS['Hindi'][season]} मौसम की फसल नहीं है।"
            }[language])

        if soil == "Unknown":
            concerns.append({
                "English": "Soil type is unknown; confirm soil suitability.",
                "Telugu": "నేల రకం తెలియదు. నేల అనుకూలతను నిర్ధారించుకోండి.",
                "Hindi": "मिट्टी का प्रकार अज्ञात है। मिट्टी की उपयुक्तता जाँचें।"
            }[language])
        elif soil in details["soils"]:
            score += 25
            reasons.append({
                "English": f"{soil} soil is a possible match.",
                "Telugu": f"{soil} నేల ఈ పంటకు అనుకూలంగా ఉండవచ్చు.",
                "Hindi": f"{soil} मिट्टी इस फसल के लिए उपयुक्त हो सकती है।"
            }[language])
        else:
            concerns.append({
                "English": f"{soil} soil may not be ideal for this crop.",
                "Telugu": f"{soil} నేల ఈ పంటకు పూర్తిగా అనుకూలం కాకపోవచ్చు.",
                "Hindi": f"{soil} मिट्टी इस फसल के लिए पूरी तरह उपयुक्त नहीं हो सकती।"
            }[language])

        if irrigation in details["water"]:
            score += 20
            reasons.append({
                "English": "Irrigation availability is compatible.",
                "Telugu": "మీ నీటి సదుపాయం ఈ పంటకు సరిపోవచ్చు.",
                "Hindi": "आपकी सिंचाई सुविधा इस फसल के लिए उपयुक्त हो सकती है।"
            }[language])
        else:
            concerns.append({
                "English": "This crop may need more reliable irrigation.",
                "Telugu": "ఈ పంటకు మరింత నమ్మకమైన నీటి సదుపాయం అవసరం కావచ్చు.",
                "Hindi": "इस फसल को अधिक विश्वसनीय सिंचाई की आवश्यकता हो सकती है।"
            }[language])

        low, high = details["temperature"]

        if low <= temperature <= high:
            score += 15
            reasons.append({
                "English": "Current temperature is within the indicative range.",
                "Telugu": "ప్రస్తుత ఉష్ణోగ్రత సూచించిన పరిధిలో ఉంది.",
                "Hindi": "वर्तमान तापमान संकेतित सीमा के भीतर है।"
            }[language])
        else:
            concerns.append({
                "English": f"Temperature is outside the indicative {low}-{high}°C range.",
                "Telugu": f"ఉష్ణోగ్రత సూచించిన {low}-{high}°C పరిధికి బయట ఉంది.",
                "Hindi": f"तापमान संकेतित {low}-{high}°C सीमा से बाहर है।"
            }[language])

        rain_low, rain_high = (0, 40)

        if rain_low <= rainfall_mm <= rain_high:
            score += 10
            reasons.append({
                "English": "Forecast rainfall is within the preliminary screening range.",
                "Telugu": "వర్షపాతం ప్రాథమిక అంచనా పరిధిలో ఉంది.",
                "Hindi": "अनुमानित वर्षा प्रारंभिक जाँच सीमा के भीतर है।"
            }[language])
        else:
            concerns.append({
                "English": "Forecast rainfall needs local assessment.",
                "Telugu": "వర్షపాతాన్ని స్థానిక పరిస్థితుల ఆధారంగా పరిశీలించాలి.",
                "Hindi": "वर्षा का स्थानीय परिस्थितियों के अनुसार आकलन आवश्यक है।"
            }[language])

        if rainfall_probability >= 70:
            concerns.append({
                "English": "High rain probability: check drainage and avoid waterlogging.",
                "Telugu": "వర్షం పడే అవకాశం ఎక్కువగా ఉంది. నీరు నిల్వ ఉండకుండా కాలువలను తనిఖీ చేయండి.",
                "Hindi": "बारिश की संभावना अधिक है। जल निकासी की जाँच करें।"
            }[language])

        result = {
            "crop": crop,
            "score": score,
            "reasons": reasons,
            "concerns": concerns,
            "general_reason": details["reason"][language],
            "water_note": details["warning"][language]
        }

        if score >= 60:
            suitable.append(result)
        else:
            less_suitable.append(result)

    suitable.sort(key=lambda item: item["score"], reverse=True)
    less_suitable.sort(key=lambda item: item["score"], reverse=True)

    return {
        "season": SEASON_TRANSLATIONS[language][season],
        "recommended": suitable[:3],
        "other_options": suitable[3:],
        "less_suitable": less_suitable
    }
