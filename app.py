import streamlit as st
from questions.important_questions import exam_zone_data
from questions.model_answers import model_answers_data
from revision.quick_revision import quick_revision_data
from questions.model_answers import save_model_answers
from analytics import log_usage
import pandas as pd
from analytics import conn

# UNIT I CONTENT
topic1 = """
## ভূ-কৌশলগত অৱস্থান আৰু সমাজ-সংস্কৃতিক বৈচিত্ৰ্য

---

### 📍 1. ভৌগোলিক কৌশলগত অৱস্থান

উত্তৰ-পূৰ্ব ভাৰত ভৌগোলিকভাৱে ভাৰতৰ এক গুৰুত্বপূৰ্ণ সীমান্ত অঞ্চল, যি দক্ষিণ এছিয়া আৰু দক্ষিণ-পূৰ্ব এছিয়াৰ মাজত সংযোগ স্থাপন কৰে।

**সীমা সংযোগ:**
- পশ্চিমে → বংগ
- উত্তৰে → চীন আৰু ভূটান
- পূবে → ম্যানমাৰ
- দক্ষিণে → বাংলাদেশ

👉 ব্ৰহ্মপুত্ৰ উপত্যকা = কৌশলগত কৰিডৰ (Strategic Corridor)

এই উপত্যকা সামৰিক গতি-বিধি, বাণিজ্যিক চলাচল আৰু প্ৰশাসনিক নিয়ন্ত্ৰণৰ বাবে অতি গুৰুত্বপূৰ্ণ।

---

👉 🧭 Visual Insight

[Image: northeast_map.png | Northeast India strategic map showing Siliguri Corridor]

### 🧭 কী দেখুৱাই?
- উত্তৰ-পূৰ্ব ভাৰতৰ ভৌগোলিক বিচ্ছিন্নতা
- Siliguri Corridor (Chicken’s Neck)
- বহিঃৰাষ্ট্ৰ সীমান্ত সংযোগ

### ⚠️ কিয় গুৰুত্বপূৰ্ণ?
- ভাৰতৰ সৈতে একমাত্ৰ স্থল সংযোগ
- সামৰিক দৃষ্টিকোণত অতি সংবেদনশীল
- যিকোনো সংঘাতে বিচ্ছিন্নতাৰ সম্ভাৱনা

### 🎯 পৰীক্ষাত কেনেকৈ ব্যৱহাৰ কৰিব?
- “ভূ-কৌশলগত অৱস্থান” উত্তৰত এই মানচিত্ৰৰ ব্যাখ্যা যোগ কৰক
- Corridor concept explain কৰক

### ⚔️ 2. ব্ৰিটিছসকলৰ কৌশলগত দৃষ্টিভংগী

ব্ৰিটিছসকলে অসমক কেৱল এটা অঞ্চল হিচাপে নহয়, বৰং এটা **buffer frontier zone** হিচাপে দেখিছিল।

**মূল লক্ষ্য:**
- বাৰ্মিজ আক্ৰমণ ৰোধ
- চীনৰ প্ৰভাৱ নিয়ন্ত্ৰণ
- সামৰিক সুৰক্ষা

---

### 💰 3. অৰ্থনৈতিক গুৰুত্ব

অসম আছিল সম্পদেৰে সমৃদ্ধ অঞ্চল:

- চাহ উদ্যোগ (Tea Plantation Economy)
- তেল (Digboi oil field)
- বন সম্পদ

👉 উপনিবেশবাদৰ মূল লক্ষ্য = সম্পদ আহৰণ (Resource Extraction)

---

### 🌐 4. সমাজ-সংস্কৃতিক বৈচিত্ৰ্য

উত্তৰ-পূৰ্ব ভাৰত বহু জাতি, ভাষা আৰু সংস্কৃতিৰ মিলনস্থল।

**প্ৰধান জনগোষ্ঠী:**
- তিব্বত-বৰ্মী ভাষাগোষ্ঠী
- আৰ্যভাষী জনগোষ্ঠী
- বিভিন্ন জনজাতি (Bodo, Naga, Mizo, Karbi)

---

### 🧩 5. ঔপনিৱেশিক বিভাজন নীতি

ব্ৰিটিছসকলে বৈচিত্ৰ্যক শাসনৰ বাবে ব্যৱহাৰ কৰিছিল।

**ব্যৱস্থা:**
- Census (জনগণনা)
- Tribal vs Non-tribal বিভাজন
- প্রশাসনিক পৃথকীকৰণ

👉 Divide and Rule নীতি

---

### 🧠 6. বিশ্লেষণ

ভৌগোলিক অৱস্থান আৰু সমাজ-সংস্কৃতিক বৈচিত্ৰ্য মিলি উত্তৰ-পূৰ্ব ভাৰতক এক জটিল ৰাজনৈতিক ক্ষেত্ৰত পৰিণত কৰিছে।

👉 অঞ্চলটো:
- কৌশলগতভাৱে গুৰুত্বপূৰ্ণ
- সামাজিকভাৱে বৈচিত্ৰময়
- ৰাজনৈতিকভাৱে সংবেদনশীল

---

### ⚖️ 7. সমালোচনামূলক দৃষ্টিভংগী

✔ বৈচিত্ৰ্য = সাংস্কৃতিক সমৃদ্ধি  
✘ ঔপনিৱেশিক ব্যৱহাৰ = বিভাজন আৰু সংঘাত  

👉 আজিৰ জাতিগত ৰাজনীতিৰ মূল এই ঐতিহাসিক ভিত্তিত নিহিত।

---

### 🔗 8. সংযোগ (Contemporary Relevance)

- সীমান্ত ৰাজনীতি (China-India tension)
- NRC আৰু নাগৰিকত্ব বিতৰ্ক
- আঞ্চলিক পৰিচয় আন্দোলন

---

### 🎯 9. Exam Focus

- উত্তৰ-পূৰ্ব ভাৰতৰ ভূ-কৌশলগত অৱস্থান ব্যাখ্যা কৰা  
- সমাজ-সংস্কৃতিক বৈচিত্ৰ্য কেনেকৈ ৰাজনীতিত পৰিণত হয়?  
- ঔপনিৱেশিক বিভাজন নীতিৰ প্ৰভাৱ বিশ্লেষণ কৰা  
"""

topic2 = """
## ঔপনিৱেশিক শাসনৰ বিস্তাৰ আৰু সুদৃঢ়ীকৰণ

---

### 📍 1. অসম দখল (১৮২৬): ঐতিহাসিক পটভূমি

১৮২৬ চনৰ ইয়ানডাবোৰ সন্ধিৰ পিছত অসম ব্ৰিটিছ শাসনৰ অধীনলৈ আহে। এইটো আহোম শাসনৰ অন্ত আৰু ঔপনিৱেশিক আধিপত্যৰ আৰম্ভণি।

**প্ৰেক্ষাপট:**
- বাৰ্মিজ আক্ৰমণৰ ফলত আহোম ৰাজ্য দুর্বল হৈছিল
- ব্ৰিটিছসকলে সামৰিক আৰু কৌশলগত সুবিধা লৈ অঞ্চল দখল কৰে

👉 ইয়ানডাবোৰ সন্ধি = অসমত ঔপনিৱেশিক শাসনৰ আৰম্ভণি

---

### 🏛 2. প্রশাসনিক পুনর্গঠন

ব্ৰিটিছ শাসনে স্থানীয় শাসন ব্যৱস্থাক সম্পূৰ্ণৰূপে পৰিবর্তন কৰে।

**মূল পৰিবর্তনসমূহ:**
- ভূমি ৰাজহ ব্যৱস্থা প্ৰৱৰ্তন
- আধুনিক আদালত আৰু পুলিচ ব্যৱস্থা
- পায়েক ব্যৱস্থা বিলুপ্ত

👉 স্থানীয় ৰাজনৈতিক কাঠামো → ঔপনিৱেশিক নিয়ন্ত্ৰণ

---

### 💰 3. অৰ্থনৈতিক নীতি: শোষণমূলক কাঠামো

#### (i) ভূমি ৰাজহ ব্যৱস্থা

- নগদ কৰ ব্যৱস্থা
- কৃষকৰ ওপৰত অধিক চাপ
- স্বাৱলম্বী কৃষি ব্যৱস্থাৰ ধ্বংস

---

#### (ii) চাহ বাগিচা অৰ্থনীতি

[Image: tea_plantation_assam.png]

- ১৮৩০ৰ দশকৰ পৰা আৰম্ভ
- প্ৰৱাসী শ্রমিক (Adivasi communities)
- কঠোৰ পৰিশ্ৰম + নিম্ন মজুৰি

👉 Plantation economy = আধুনিক পুঁজিবাদী শোষণৰ উদাহৰণ

---

#### (iii) তেল আৰু বন সম্পদ

- ডিগবৈ (Digboi) তেল ক্ষেত্ৰ
- কাঠ আৰু বন সম্পদ আহৰণ

👉 অসম = সম্পদ আহৰণৰ উপনিবেশ (Resource Extraction Colony)

---

#### (iv) অফিম একচেটিয়া ব্যৱসায়

- ব্ৰিটিছ ৰাজহৰ মুখ্য উৎস
- সামাজিক ক্ষতি আৰু আসক্তি বৃদ্ধি

---

### 📊 4. অৰ্থনৈতিক কাঠামোৰ বৈশিষ্ট্য

- Export-oriented economy
- Local developmentৰ অভাৱ
- External capital dominance

---

### 🧠 5. বিশ্লেষণ

ঔপনিৱেশিক অৰ্থনীতিৰ মূল লক্ষ্য আছিল:

👉 উন্নয়ন নহয়, শোষণ

অসমত গঢ়ি উঠা অৰ্থনৈতিক কাঠামো আছিল:
- একমুখী (mono-crop economy)
- বহিৰ্মুখী (export-oriented)
- অসমতা-সৃষ্টিকারী

---

### ⚖️ 6. সমালোচনামূলক দৃষ্টিভংগী

✔ আধুনিক প্রশাসনিক কাঠামো স্থাপন হৈছিল  
✘ কিন্তু স্থানীয় অৰ্থনীতি আৰু সমাজ ক্ষতিগ্ৰস্ত হৈছিল  

👉 “Colonial modernity” = উন্নয়ন + শোষণ (দ্বৈত স্বৰূপ)

---

### 🔗 7. সমসাময়িক সংযোগ

- Tea garden labour issues (today)
- Regional economic imbalance
- Resource control debates

---

### 🗺️ 8. ভিজুৱেল বুজাবুজি

[Image: colonial_economy_flowchart.png]

👉 দেখুৱাব:
- সম্পদ আহৰণ → ৰপ্তানি → লাভ → ব্ৰিটিছৰ হাতত কেন্দ্ৰীভূত

---

### 🎯 9. Exam Focus

- ঔপনিৱেশিক শাসনৰ বৈশিষ্ট্য আলোচনা কৰা  
- অসমত চাহ বাগিচা অৰ্থনীতিৰ প্ৰভাৱ বিশ্লেষণ কৰা  
- ঔপনিৱেশিক অৰ্থনীতি “শোষণমূলক” বুলি কেনেকৈ কোৱা হয়?  
"""

topic3 = """
## Excluded আৰু Partially Excluded অঞ্চল: Inner Line আৰু ঔপনিৱেশিক সীমান্ত নীতি

---

### 📍 1. পৰিচয়

উত্তৰ-পূৰ্ব ভাৰতত ব্ৰিটিছ শাসনে এক বিশেষ ধৰণৰ প্রশাসনিক নীতি গ্ৰহণ কৰিছিল, যাৰ উদ্দেশ্য আছিল সীমান্ত নিয়ন্ত্ৰণ, জনজাতীয় অঞ্চল সুৰক্ষা আৰু শাসন সহজ কৰা।

👉 এই নীতিৰ কেন্দ্ৰত আছিল:
- Inner Line Regulation (1873)
- Excluded আৰু Partially Excluded Areas (1935)

---

### 📜 2. Inner Line Regulation, 1873

এই বিধি অনুসাৰে:

- পাহাৰীয়া অঞ্চলত বহিঃলোকৰ প্ৰৱেশ নিয়ন্ত্ৰণ কৰা হৈছিল
- জনজাতীয় ভূমি সংৰক্ষণ কৰা হৈছিল
- ব্ৰিটিছ প্ৰশাসন সীমান্ত নিয়ন্ত্ৰণ কৰিছিল

👉 অনুমতি অবিহনে বহিঃলোক প্ৰৱেশ কৰিব নোৱাৰিছিল

---

### 🗺️ ভিজুৱেল বুজাবুজি

[Image: inner_line_map.png]

👉 এই মানচিত্ৰত দেখুৱাব:
- Inner Line এলাকা
- পাহাৰ বনাম সমতল বিভাজন
- প্রশাসনিক সীমা

---

### ⚠️ 3. প্ৰভাৱ

#### (i) ইতিবাচক দিশ
- জনজাতীয় সংস্কৃতি সংৰক্ষণ
- বহিঃলোকৰ শোষণৰ পৰা সুৰক্ষা

#### (ii) নেতিবাচক দিশ
- পাহাৰ আৰু সমতল অঞ্চলৰ মাজত বিভাজন
- সামাজিক আৰু অৰ্থনৈতিক দূৰত্ব বৃদ্ধি

👉 “Isolation with protection”

---

### 📜 4. Government of India Act, 1935

এই আইনে অঞ্চলসমূহক ভাগ কৰে:

- Excluded Areas
- Partially Excluded Areas

---

### ⚙️ বৈশিষ্ট্য

- বিধানসভাৰ ক্ষমতা সীমিত
- গৱৰ্ণৰৰ বিশেষ ক্ষমতা
- গণতান্ত্ৰিক প্ৰক্ৰিয়া প্ৰায় নাই

👉 কেন্দ্ৰৰ সোজা নিয়ন্ত্ৰণ

---

### 📊 5. Excluded vs Partially Excluded

| বৈশিষ্ট্য | Excluded Area | Partially Excluded |
|----------|--------------|-------------------|
| বিধানসভা | প্ৰযোজ্য নহয় | সীমিত |
| গৱৰ্ণৰ ক্ষমতা | সম্পূৰ্ণ | আংশিক |
| গণতন্ত্ৰ | নাই | সীমিত |

---

### 🧠 6. বিশ্লেষণ

এই নীতিসমূহৰ দ্বৈত উদ্দেশ্য আছিল:

👉 সুৰক্ষা + নিয়ন্ত্ৰণ

কিন্তু বাস্তৱত ই সৃষ্টি কৰিছিল:

- ৰাজনৈতিক বিচ্ছিন্নতা
- বিকাশৰ বাধা
- আঞ্চলিক অসমতা

---

### ⚖️ 7. সমালোচনামূলক দৃষ্টিভংগী

✔ জনজাতীয় স্বাৰ্থ ৰক্ষা কৰিছিল  
✘ কিন্তু মূল ৰাজনৈতিক প্ৰবাহত অংশগ্ৰহণৰ পৰা বঞ্চিত কৰিছিল  

👉 “Protective exclusion” = উন্নয়নৰ বাধা

---

### 🔗 8. সমসাময়িক সংযোগ

- ILP (Inner Line Permit) আজিও প্ৰযোজ্য (Nagaland, Mizoram, Arunachal)
- নাগৰিকত্ব আৰু ভূমি অধিকাৰ বিতৰ্ক
- কেন্দ্র-ৰাজ্য সম্পর্ক

---

### 🧩 9. তাত্ত্বিক ব্যাখ্যা

এই নীতিসমূহক কোৱা হয়:

👉 Frontier Policy

য’ত:
- অঞ্চলক সম্পূৰ্ণ একত্ৰিত কৰা নহয়
- কিন্তু সম্পূৰ্ণ স্বাধীনো নহয়

---

### 🎯 10. Exam Focus

- Inner Line Regulation ব্যাখ্যা কৰা  
- Excluded আৰু Partially Excluded অঞ্চলৰ পাৰ্থক্য লিখা  
- এই নীতিয়ে উত্তৰ-পূৰ্ব ভাৰতৰ ৰাজনীতিত কেনে প্ৰভাৱ পেলালে?  
"""

topic4 = """
## ঔপনিৱেশিক বিৰোধী বিদ্ৰোহ আৰু স্বাধীনতা আন্দোলনৰ ভেটি

---

### 📍 1. পৰিচয়

অসমত ঔপনিৱেশিক শাসনৰ বিৰুদ্ধে প্ৰাথমিক প্ৰতিবাদসমূহ কৃষক আৰু স্থানীয় জনগোষ্ঠীৰ মাজৰ পৰা আৰম্ভ হৈছিল।

এইবোৰ কেৱল স্বতঃস্ফূৰ্ত বিদ্ৰোহ নহয়,  
👉 ই আছিল ঔপনিৱেশিক শোষণৰ বিৰুদ্ধে সংগঠিত প্ৰতিক্ৰিয়া।

---

### ⚔️ 2. ফুলাগুৰি ঢেৱা (১৮৬১)

#### 📌 কাৰণ

- সুপাৰিৰ ওপৰত কৰ আৰোপ
- কৃষকৰ ওপৰত অৰ্থনৈতিক চাপ
- ব্ৰিটিছ ৰাজহ নীতিৰ বিৰুদ্ধে অসন্তোষ

---

#### 📌 ঘটনা

- কৃষকৰ সমবেত সভা
- প্ৰতিবাদ
- ব্ৰিটিছ প্ৰশাসনৰ দমন

---

#### 👉 তাৎপর্য

- অসমৰ প্ৰথম সংগঠিত কৃষক বিদ্ৰোহ
- স্থানীয় প্ৰতিবাদৰ ৰাজনৈতিক ৰূপ

---

### ⚔️ 3. পথাৰুঘাট বিদ্ৰোহ (১৮৯৪)

#### 📌 কাৰণ

- ৭০% ভূমি ৰাজহ বৃদ্ধি
- কৃষকৰ জীৱন সংকট

---

#### 📌 ঘটনা

- হাজাৰ হাজাৰ কৃষকৰ সমাবেশ
- পুলিচৰ গুলিচালনা
- বহু লোক নিহত

---

#### 👉 তাৎপর্য

- “অসমৰ জালিয়ানৱালা বাগ” (প্ৰতীকী)
- গণপ্ৰতিক্ৰিয়াৰ স্পষ্ট প্ৰকাশ

---

### 🗺️ ভিজুৱেল বুজাবুজি

[Image: patharughat_massacre.png | Patharughat firing place memorial]

👉 দেখুৱাব:
- সমাবেশ স্থান
- গুলিচালনা
- জনসমাবেশৰ পৰিমাণ

---

### 📊 4. বিদ্ৰোহসমূহৰ সাধাৰণ বৈশিষ্ট্য

- কৃষক-ভিত্তিক আন্দোলন
- অৰ্থনৈতিক কাৰণ
- সংগঠিত প্ৰতিবাদ
- স্থানীয় নেতৃত্ব

---

### 🧠 5. বিশ্লেষণ: Proto-Nationalism

এই বিদ্ৰোহসমূহক “proto-nationalism” বুলি কোৱা হয়।

👉 কাৰণ:
- জাতীয় আন্দোলনৰ পূৰ্বসূচনা
- ঔপনিৱেশিক শাসনৰ বিৰুদ্ধে সচেতনতা
- গণপ্ৰতিক্ৰিয়াৰ আৰম্ভণি

---

### 🇮🇳 6. স্বাধীনতা আন্দোলনৰ সৈতে সংযোগ

এই বিদ্ৰোহসমূহে পৰৱৰ্তী বৃহৎ আন্দোলনৰ ভিত্তি স্থাপন কৰে:

- অসম এছ’চিয়েচন (1903)
- অসহযোগ আন্দোলন (1920)
- ভাৰত ছাড়ো আন্দোলন (1942)

👉 স্থানীয় আন্দোলন → জাতীয়তাবাদ

---

### ⚖️ 7. সমালোচনামূলক দৃষ্টিভংগী

✔ সংগঠিত প্ৰতিবাদৰ সূচনা  
✔ ৰাজনৈতিক সচেতনতা বৃদ্ধি  

✘ কিন্তু:
- সীমিত বিস্তৃতি
- কেন্দ্ৰীয় নেতৃত্বৰ অভাৱ

---

### 🔗 8. সমসাময়িক সংযোগ

- কৃষক আন্দোলনৰ ঐতিহাসিক ধাৰাবাহিকতা
- স্থানীয় বনাম কেন্দ্ৰ শাসন দ্বন্দ্ব
- গণপ্ৰতিক্ৰিয়াৰ ৰাজনীতি

---

### 🎯 9. Exam Focus

- ফুলাগুৰি ঢেৱা আৰু পথাৰুঘাট বিদ্ৰোহৰ কাৰণ আৰু তাৎপর্য লিখা  
- এই বিদ্ৰোহসমূহ কেনেকৈ জাতীয়তাবাদৰ ভেটি স্থাপন কৰিলে?  
- “Proto-nationalism” বুলিলে কি বুজায়?  
"""

# UNIT II CONTENT
unit2_topic1 = """
## অসম আন্দোলন (1979–1985)

---

### 📍 পৰিচয়

অসম আন্দোলন আছিল বিদেশী অনুপ্ৰৱেশৰ বিৰুদ্ধে গণআন্দোলন।

---

### ⚠️ কাৰণ

- অবৈধ প্ৰৱ্ৰজন (বিশেষকৈ বাংলাদেশৰ পৰা)
- ভোটাৰ তালিকাত বিদেশীৰ অন্তৰ্ভুক্তি
- স্থানীয় জনগোষ্ঠীৰ পৰিচয় সংকট

---

### 👥 নেতৃত্ব

- AASU (All Assam Students’ Union)
- All Assam Gana Sangram Parishad

---

### 📆 মুখ্য ঘটনা

- ১৯৭৯ → আন্দোলনৰ আৰম্ভণি
- ১৯৮৩ → হিংসাত্মক নিৰ্বাচন
- ১৯৮৫ → অসম চুক্তি

---

### 📜 অসম চুক্তি (1985)

- 1971 cutoff date
- বিদেশী চিনাক্তকৰণ আৰু বহিষ্কাৰ

---

### 👉 মূল তাৎপর্য

- গণ আন্দোলনৰ শক্তি
- আঞ্চলিক ৰাজনীতিৰ উত্থান

---

### 🧠 বিশ্লেষণ

এই আন্দোলন পৰিচয় ৰাজনীতিৰ এক শক্তিশালী উদাহৰণ।

---

### ⚖️ সমালোচনামূলক দৃষ্টিভংগী

✔ স্থানীয় অধিকাৰ ৰক্ষা  
✘ কিন্তু হিংসা আৰু বিভাজন বৃদ্ধি

---

### 🎯 Exam Focus

- অসম আন্দোলনৰ কাৰণ আৰু পৰিণাম
- অসম চুক্তিৰ বৈশিষ্ট্য
"""

unit2_topic2 = """
## অসম আন্দোলন (1979–1985)

---

### 📍 পৰিচয়

অসম আন্দোলন আছিল বিদেশী অনুপ্ৰৱেশৰ বিৰুদ্ধে গণআন্দোলন।

---

### ⚠️ কাৰণ

- অবৈধ প্ৰৱ্ৰজন (বিশেষকৈ বাংলাদেশৰ পৰা)
- ভোটাৰ তালিকাত বিদেশীৰ অন্তৰ্ভুক্তি
- স্থানীয় জনগোষ্ঠীৰ পৰিচয় সংকট

---

### 👥 নেতৃত্ব

- AASU (All Assam Students’ Union)
- All Assam Gana Sangram Parishad

---

### 📆 মুখ্য ঘটনা

- ১৯৭৯ → আন্দোলনৰ আৰম্ভণি
- ১৯৮৩ → হিংসাত্মক নিৰ্বাচন
- ১৯৮৫ → অসম চুক্তি

---

### 📜 অসম চুক্তি (1985)

- 1971 cutoff date
- বিদেশী চিনাক্তকৰণ আৰু বহিষ্কাৰ

---

### 👉 মূল তাৎপর্য

- গণ আন্দোলনৰ শক্তি
- আঞ্চলিক ৰাজনীতিৰ উত্থান

---

### 🧠 বিশ্লেষণ

এই আন্দোলন পৰিচয় ৰাজনীতিৰ এক শক্তিশালী উদাহৰণ।

---

### ⚖️ সমালোচনামূলক দৃষ্টিভংগী

✔ স্থানীয় অধিকাৰ ৰক্ষা  
✘ কিন্তু হিংসা আৰু বিভাজন বৃদ্ধি

---

### 🎯 Exam Focus

- অসম আন্দোলনৰ কাৰণ আৰু পৰিণাম
- অসম চুক্তিৰ বৈশিষ্ট্য
"""

unit2_topic3 = """
## বড়ো আন্দোলন (Bodo Movement)

---

### 📍 পৰিচয়

বড়ো আন্দোলন আছিল স্বায়ত্তশাসন আৰু পৃথক ৰাজ্যৰ দাবীৰ আন্দোলন।

---

### 🎯 মুখ্য দাবী

- পৃথক বড়োলেণ্ড ৰাজ্য
- সাংস্কৃতিক স্বীকৃতি
- ৰাজনৈতিক অধিকাৰ

---

### 👥 সংগঠন

- ABSU (All Bodo Students’ Union)
- NDFB (armed group)

---

### 📜 বড়ো চুক্তিসমূহ

- 1993 → Bodo Autonomous Council
- 2003 → BTC (Bodoland Territorial Council)
- 2020 → নতুন চুক্তি

---

### 👉 মূল তাৎপর্য

- স্বায়ত্তশাসনৰ ৰাজনীতি
- জাতিগত আন্দোলনৰ বিকাশ

---

### 🧠 বিশ্লেষণ

এই আন্দোলনে "ethnic assertion" ৰ শক্তি দেখুৱাইছে।

---

### ⚖️ সমালোচনামূলক দৃষ্টিভংগী

✔ স্বায়ত্তশাসন লাভ  
✘ অভ্যন্তৰীণ সংঘাত আৰু বিভাজন

---

### 🎯 Exam Focus

- বড়ো আন্দোলনৰ বিকাশ
- বড়ো চুক্তিৰ মূল্যায়ন
"""

# UNIT III CONTENT
unit3_topic1 = """
## জাতিগত আন্দোলন (Ethnic Movements in Northeast India)

---

### 📍 পৰিচয়

উত্তৰ-পূৰ্ব ভাৰতত জাতিগত আন্দোলনসমূহ পৰিচয়, ভূমি আৰু ৰাজনৈতিক অধিকাৰৰ সৈতে জড়িত।

---

### ⚠️ মুখ্য কাৰণ

- সাংস্কৃতিক পৰিচয় সংকট
- ভূমি অধিকাৰৰ সমস্যা
- বহিৰাগত অনুপ্ৰৱেশ
- উন্নয়নৰ অভাৱ

---

### 📊 মুখ্য আন্দোলনসমূহ

- নাগা আন্দোলন
- মিজো আন্দোলন
- বড়ো আন্দোলন

👉 সকলো আন্দোলনৰ কেন্দ্ৰত “identity assertion”

---

### 👉 মূল ধাৰণা

জাতিগত ৰাজনীতি = পৰিচয় + সম্পদ + ক্ষমতা

---

### 🧠 বিশ্লেষণ

এই আন্দোলনসমূহ কেৱল বিচ্ছিন্নতা নহয়,  
ই "recognition politics" ৰ অংশ।

---

### ⚖️ সমালোচনামূলক দৃষ্টিভংগী

✔ পৰিচয় ৰক্ষা  
✘ আঞ্চলিক সংঘাত বৃদ্ধি  

---

### 🎯 Exam Focus

- জাতিগত আন্দোলনৰ কাৰণ আৰু বৈশিষ্ট্য
- নাগা আৰু মিজো আন্দোলনৰ তুলনা
"""

unit3_topic2 = """
## স্বায়ত্তশাসিত পৰিষদ (Autonomy Councils)

---

### 📍 পৰিচয়

উত্তৰ-পূৰ্ব ভাৰতত বিভিন্ন জনজাতিক স্বায়ত্তশাসন প্ৰদানৰ বাবে পৰিষদ গঠন কৰা হৈছে।

---

### 📜 সাংবিধানিক ভিত্তি

👉 ভাৰতৰ সংবিধানৰ ষষ্ঠ তফসিল

---

### 🏛 উদাহৰণ

- BTC (Bodoland Territorial Council)
- Karbi Anglong Autonomous Council
- Khasi Hills Council

---

### ⚙️ ক্ষমতা

- ভূমি ব্যৱস্থাপনা
- স্থানীয় শাসন
- সংস্কৃতি সংৰক্ষণ

---

### 👉 মূল ধাৰণা

Decentralization of power

---

### 🧠 বিশ্লেষণ

এই পৰিষদসমূহ কেন্দ্ৰ আৰু স্থানীয় জনগোষ্ঠীৰ মাজত সমন্বয় সৃষ্টি কৰে।

---

### ⚖️ সমালোচনামূলক দৃষ্টিভংগী

✔ স্থানীয় স্বায়ত্তশাসন  
✘ সীমিত ক্ষমতা আৰু ৰাজনৈতিক দ্বন্দ্ব  

---

### 🎯 Exam Focus

- ষষ্ঠ তফসিলৰ বৈশিষ্ট্য
- স্বায়ত্তশাসিত পৰিষদৰ ভূমিকা
"""

unit3_topic3 = """
## আঞ্চলিক আন্দোলন আৰু আকাংক্ষা (Regional Aspirations)

---

### 📍 পৰিচয়

উত্তৰ-পূৰ্ব ভাৰতত আঞ্চলিক আন্দোলনসমূহ বিকাশ হৈছে উন্নয়ন আৰু পৰিচয়ৰ দাবীৰ ভিত্তিত।

---

### ⚠️ মুখ্য কাৰণ

- অৰ্থনৈতিক পশ্চাৎপদতা
- উন্নয়নৰ অসম বণ্টন
- ৰাজনৈতিক অবহেলা

---

### 📊 উদাহৰণ

- পৃথক ৰাজ্যৰ দাবী
- স্বায়ত্তশাসনৰ দাবী
- সাংস্কৃতিক স্বীকৃতিৰ আন্দোলন

---

### 👉 মূল ধাৰণা

Regionalism = উন্নয়ন + পৰিচয় + ক্ষমতা

---

### 🧠 বিশ্লেষণ

আঞ্চলিক আন্দোলনসমূহ কেন্দ্ৰ-ৰাজ্য সম্পৰ্কৰ ফল।

---

### ⚖️ সমালোচনামূলক দৃষ্টিভংগী

✔ উন্নয়নৰ দাবী  
✘ বিভাজনমূলক ৰাজনীতি  

---

### 🎯 Exam Focus

- আঞ্চলিক আন্দোলনৰ কাৰণ
- আঞ্চলিক ৰাজনীতিৰ প্ৰভাৱ
"""

# UNIT IV CONTENT

unit4_topic1 = """
## উত্তৰ-পূৰ্ব ভাৰতত বিদ্ৰোহ (Insurgency in Northeast India)

---

### 📍 পৰিচয়

উত্তৰ-পূৰ্ব ভাৰতত বিদ্ৰোহ (insurgency) হৈছে ৰাজনৈতিক, জাতিগত আৰু ঐতিহাসিক কাৰণসমূহৰ ফল।

---

### ⚠️ মুখ্য কাৰণ

- পৰিচয় সংকট
- ৰাজনৈতিক অবহেলা
- অৰ্থনৈতিক পশ্চাৎপদতা
- ঐতিহাসিক অসন্তোষ

---

### 📊 মুখ্য সংগঠন

- ULFA (Assam)
- NSCN (Nagaland)
- NDFB (Bodoland)

👉 Armed nationalism ৰ উদাহৰণ

---

### 👉 মূল ধাৰণা

Insurgency = Political dissatisfaction + Identity crisis

---

### 🧠 বিশ্লেষণ

এই বিদ্ৰোহসমূহ কেন্দ্ৰৰ সৈতে আঞ্চলিক দ্বন্দ্বৰ ফল।

---

### ⚖️ সমালোচনামূলক দৃষ্টিভংগী

✔ পৰিচয় দাবী  
✘ হিংসা আৰু অস্থিতিশীলতা  

---

### 🎯 Exam Focus

- উত্তৰ-পূৰ্ব ভাৰতত বিদ্ৰোহৰ কাৰণ
- ULFA ৰ উত্থান ব্যাখ্যা কৰা
"""

unit4_topic2 = """
## শান্তি চুক্তি (Peace Accords)

---

### 📍 পৰিচয়

বিদ্ৰোহ সমাধানৰ বাবে কেন্দ্ৰ চৰকাৰ আৰু সংগঠনসমূহৰ মাজত শান্তি চুক্তি সম্পন্ন কৰা হৈছে।

---

### 📜 মুখ্য চুক্তিসমূহ

- Assam Accord (1985)
- Mizo Accord (1986)
- Bodo Accord (1993, 2003, 2020)

---

### 🎯 উদ্দেশ্য

- হিংসা বন্ধ কৰা
- ৰাজনৈতিক সমাধান
- উন্নয়ন নিশ্চিত কৰা

---

### 👉 মূল ধাৰণা

Peace-building process

---

### 🧠 বিশ্লেষণ

এই চুক্তিসমূহ সম্পূৰ্ণ সমাধান নহয়,  
কিন্তু সংঘাত নিয়ন্ত্ৰণৰ প্ৰচেষ্টা।

---

### ⚖️ সমালোচনামূলক দৃষ্টিভংগী

✔ শান্তি প্ৰতিষ্ঠা  
✘ সকলো সমস্যাৰ সমাধান নহয়  

---

### 🎯 Exam Focus

- অসম চুক্তি আৰু মিজো চুক্তি তুলনা কৰা
- শান্তি চুক্তিৰ সফলতা মূল্যায়ন কৰা
"""

unit4_topic3 = """
## সুৰক্ষা আৰু শাসন (Security and Governance)

---

### 📍 পৰিচয়

উত্তৰ-পূৰ্ব ভাৰতত সুৰক্ষা আৰু শাসন প্ৰশ্ন বিদ্ৰোহ আৰু ৰাজনৈতিক সমস্যাৰ সৈতে জড়িত।

---

### ⚙️ সুৰক্ষা ব্যৱস্থা

- AFSPA (Armed Forces Special Powers Act)
- সেনা আৰু আধাসামৰিক বাহিনী

---

### 🏛 শাসন সমস্যা

- দূৰ্বল শাসন ব্যৱস্থা
- উন্নয়নৰ অভাৱ
- ৰাজনৈতিক অস্থিৰতা

---

### 👉 মূল ধাৰণা

Security vs Democracy dilemma

---

### 🧠 বিশ্লেষণ

সুৰক্ষা আৰু গণতান্ত্ৰিক অধিকাৰৰ মাজত সমতা ৰক্ষা কৰাটো এক ডাঙৰ চ্যালেঞ্জ।

---

### ⚖️ সমালোচনামূলক দৃষ্টিভংগী

✔ সুৰক্ষা নিশ্চিত কৰে  
✘ নাগৰিক অধিকাৰ হ্ৰাস কৰে  

---

### 🎯 Exam Focus

- AFSPA ৰ পক্ষে-বিপক্ষে যুক্তি
- উত্তৰ-পূৰ্ব ভাৰতত শাসনৰ সমস্যা আলোচনা কৰা
"""

all_units = {
    "Unit I": {
        "ভূ-কৌশলগত অৱস্থান আৰু সমাজ-সংস্কৃতিক বৈচিত্ৰ্য": topic1,
        "ঔপনিৱেশিক শাসনৰ বিস্তাৰ আৰু সুদৃঢ়ীকৰণ": topic2,
        "Excluded আৰু Partially Excluded অঞ্চল": topic3,
        "ঔপনিৱেশিক বিৰোধী বিদ্ৰোহ": topic4
    },

        "Unit II": {
        "ভাষা ৰাজনীতি": unit2_topic1,
        "অসম আন্দোলন": unit2_topic2,
        "বড়ো আন্দোলন": unit2_topic3
    },

        "Unit III": {
        "জাতিগত আন্দোলন": unit3_topic1,
        "স্বায়ত্তশাসিত পৰিষদ": unit3_topic2,
        "আঞ্চলিক আন্দোলন": unit3_topic3
    },

        "Unit IV": {
        "বিদ্ৰোহ": unit4_topic1,
        "শান্তি চুক্তি": unit4_topic2,
        "সুৰক্ষা আৰু শাসন": unit4_topic3
    }
}
import os
import json
import sys
from pprint import pformat
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO
from pathlib import Path
from PIL import Image


if "menu" not in st.session_state:
    st.session_state["menu"] = None
if "selected_unit" not in st.session_state:
    st.session_state["selected_unit"] = None
if "selected_topic" not in st.session_state:
    st.session_state["selected_topic"] = None

def render_academic_block(text):
    import markdown

    lines = text.strip().split("\n")
    title = lines[0]
    body = "\n".join(lines[1:])
    html_body = markdown.markdown(body)

    if "Exam Focus" in title or "🎯" in title:
        color = "#0d6efd"
        label = "🎯 Exam Focus"
    elif "Visual" in title or "🧭" in title:
        color = "#198754"
        label = "🧭 Visual Insight"
    elif "Analysis" in title or "বিশ্লেষণ" in title:
        color = "#6f42c1"
        label = "🧠 Analysis"
    elif "Critical" in title or "সমালোচনামূলক" in title:
        color = "#dc3545"
        label = "⚖️ Critical View"
    else:
        color = "#6c757d"
        label = title

    html = f"""
<div style="border-left: 5px solid {color}; padding: 12px; margin: 10px 0; background-color: #f8f9fa; border-radius: 6px;">
<strong>{label}</strong><br>
{html_body}
</div>
"""

    st.markdown(html, unsafe_allow_html=True)

def render_units(data):

    units = list(data.keys())

    selected_unit = st.selectbox(
        "Unit নিৰ্বাচন কৰক",
        units,
        key="unit_selector"
    )

    content_block = data[selected_unit]

    st.markdown("---")

    # CASE 1: dict (Study / Exam / Model)
    if isinstance(content_block, dict):

        topics = list(content_block.keys())

        selected_topic = st.selectbox(
            "বিষয় নিৰ্বাচন কৰক",
            topics,
            key="topic_selector"
        )

        content = content_block[selected_topic]
        log_usage("study", selected_unit, selected_topic)

        # Sub-case A: text
        if isinstance(content, str):
            st.write(content)

        # Sub-case B: list (Exam Zone)
        elif isinstance(content, list):
            for item in content:
                st.markdown(f"- {item}")

        # Sub-case C: nested dict (Model Answers)
        elif isinstance(content, dict):
            for q, ans in content.items():
                st.markdown(f"**{q}**")
                st.markdown(ans)
                st.markdown("---")

    # CASE 2: list (Quick Revision)
    elif isinstance(content_block, list):
        for item in content_block:
            st.markdown(f"- {item}")



# from content.unit1 import unit1_data
# from content.unit2 import unit2_data
# from content.unit3 import unit3_data
# from content.unit4 import unit4_data

BASE_DIR = Path(__file__).resolve().parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from questions.important_questions import exam_zone_data
from questions.model_answers import model_answers_data
from content.references import reference_data
from revision.quick_revision import quick_revision_data
FACULTY_PASSWORD = "Hybrid2030"
important_questions = exam_zone_data

def create_pdf(title, content):
    buffer = BytesIO()

    pdfmetrics.registerFont(
        TTFont(
            "AssameseFont",
            str(BASE_DIR / "NotoSansBengali-VariableFont_wdth,wght.ttf")
        )
    )

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.fontName = "AssameseFont"
    title_style.fontSize = 16

    body_style = styles["Normal"]
    body_style.fontName = "AssameseFont"
    body_style.fontSize = 12
    body_style.leading = 18

    story = []

    story.append(
        Paragraph(title, title_style)
    )

    story.append(
        Spacer(1, 20)
    )

    for paragraph in content.split("\n"):
        if paragraph.strip():
            story.append(
                Paragraph(paragraph, body_style)
            )
            story.append(
                Spacer(1, 10)
            )

    doc.build(story)

    buffer.seek(0)
    return buffer

def load_visual_panel(image_name, panel=None):
    image_path = BASE_DIR / "images" / image_name

    with Image.open(image_path) as image:
        if panel is None:
            return image.copy()

        width, height = image.size
        half_width = width // 2
        half_height = height // 2

        crop_boxes = {
            "top_left": (0, 0, half_width, half_height),
            "top_right": (half_width, 0, width, half_height),
            "bottom_left": (0, half_height, half_width, height),
            "bottom_right": (half_width, half_height, width, height),
        }

        return image.crop(crop_boxes[panel]).copy()
st.set_page_config(
    page_title="POL060304",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------------
# MASTER CONTENT MAP
# -----------------------------------

file_path = os.path.join(str(BASE_DIR), "data", "notes.json")
important_questions_file_path = BASE_DIR / "questions" / "important_questions.py"

def load_notes_data():
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_notes_data(notes_data):
    temp_file_path = f"{file_path}.tmp"

    with open(temp_file_path, "w", encoding="utf-8") as f:
        json.dump(
            notes_data,
            f,
            ensure_ascii=False,
            indent=4
        )
        f.flush()
        os.fsync(f.fileno())

    os.replace(temp_file_path, file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_important_questions_data(question_data):
    temp_file_path = f"{important_questions_file_path}.tmp"
    serialized_data = "exam_zone_data = " + pformat(
        question_data,
        width=120,
        sort_dicts=False
    ) + "\n"

    with open(temp_file_path, "w", encoding="utf-8") as f:
        f.write(serialized_data)
        f.flush()
        os.fsync(f.fileno())

    os.replace(temp_file_path, important_questions_file_path)

all_units = load_notes_data()

query_params = st.query_params
selected_state = query_params.get("state", "home")

if isinstance(selected_state, list):
    selected_state = selected_state[0]

selected_state = str(selected_state).strip().lower()

state_pages = {
    "assam": ("Assam (অসম)", "Welcome to the Assam Textbook and Paper section."),
    "arunachal": ("Arunachal Pradesh", "Welcome to the Arunachal Pradesh Paper section."),
    "manipur": ("Manipur", "Welcome to the Manipur Paper section."),
    "meghalaya": ("Meghalaya", "Welcome to the Meghalaya Paper section."),
    "mizoram": ("Mizoram", "Welcome to the Mizoram Paper section."),
    "nagaland": ("Nagaland", "Welcome to the Nagaland Paper section."),
    "sikkim": ("Sikkim", "Welcome to the Sikkim Paper section."),
    "tripura": ("Tripura", "Welcome to the Tripura Paper section.")
}

st.sidebar.title("বিভাগ নির্বাচন কৰক")
st.sidebar.subheader("Select State")

if selected_state != "home":
    if selected_state in state_pages:
        state_title, state_message = state_pages[selected_state]
        st.title(state_title)
        st.write(state_message)
    else:
        st.title("Northeast Textbook & Papers")
        st.write("Select a state from the Android Menu to view specific papers.")

    st.stop()


# -----------------------------------
# HEADER
# -----------------------------------

st.image("images/logo.png", width=90)

st.markdown("## POL060304")
st.markdown("### Politics in Northeast India")

st.markdown("**B.P. Chaliha College (BPC)**  \nBA 6th Semester Academic Learning Platform")

st.caption("Version 1.0 • Updated for Academic Session 2026")

st.info("Faculty-guided academic support for study materials, exam preparation, model answers, revision, and visual learning.")

st.markdown("---")

# -----------------------------------
# MAIN MENU
# -----------------------------------

if "menu" not in st.session_state:
    st.session_state.menu = "পাঠ্য সামগ্ৰী"

col1, col2 = st.columns(2)

with col1:
    if st.button("📘 Study Materials", use_container_width=True):
        st.session_state.menu = "পাঠ্য সামগ্ৰী"

    if st.button("📝 Exam Zone", use_container_width=True):
        st.session_state.menu = "Exam Zone"

    if st.button("📄 Model Answers", use_container_width=True):
        st.session_state.menu = "Model Answers"

    if st.button("⚡ Quick Revision", use_container_width=True):
        st.session_state.menu = "দ্ৰুত পুনৰালোচনা"

with col2:
    if st.button("🗺 Visual Learning Zone", use_container_width=True):
        st.session_state.menu = "Visual Learning Zone"

    if st.button("🔍 Search Topic", use_container_width=True):
        st.session_state.menu = "Search Topic"

    if st.button("👨‍🏫 Faculty Admin", use_container_width=True):
        st.session_state.menu = "Faculty Admin"

    if st.button("ℹ About & Disclaimer", use_container_width=True):
        st.session_state.menu = "About & Disclaimer"

menu = st.session_state.get("menu")

# -----------------------------------


if menu == "পাঠ্য সামগ্ৰী":

    render_units(all_units)


# -----------------------------------
# IMPORTANT QUESTIONS
# -----------------------------------
if menu == "Search Topic":

    st.title("Smart Topic Finder")

    st.write("Quickly find important topics from your semester content.")

    search_unit = st.selectbox(
        "Select Unit",
        ["All Units"] + list(all_units.keys())
    )

    search_keyword = st.text_input(
        "Enter topic keyword"
    )
    normalized_keyword = search_keyword.strip().lower()

    st.markdown("---")

    results_found = False

    if normalized_keyword:
        for unit_name, topics in all_units.items():

            if search_unit != "All Units" and unit_name != search_unit:
                continue

            for topic_name, topic_content in topics.items():

                if (
                    normalized_keyword in topic_name.lower()
                    or normalized_keyword in topic_content.lower()
                ):

                    results_found = True

                    st.subheader(f"{unit_name} → {topic_name}")
                    render_academic_block(topic_content[:500])

                    if st.button(
                        f"Open Full Topic: {topic_name}",
                        key=topic_name
                    ):
                        st.session_state["selected_unit"] = unit_name
                        st.session_state["selected_topic"] = topic_name
                        st.session_state["menu"] = "পাঠ্য সামগ্ৰী"
                        st.rerun()

    if normalized_keyword and not results_found:
        st.warning("No matching topic found.")

elif menu == "Exam Zone":
    render_units(exam_zone_data)
    
# -----------------------------------
# QUICK REVISION
# -----------------------------------
elif menu == "Model Answers": 
  render_units(model_answers_data)

elif menu == "দ্ৰুত পুনৰালোচনা":

    st.header("⚡ Quick Revision")

    selected_unit = st.selectbox(
        "ইউনিট নিৰ্বাচন কৰক",
        list(quick_revision_data.keys()),
        key="revision_unit"
    )

    st.markdown("---")

    for item in quick_revision_data[selected_unit]:
        st.markdown(f"- {item}")

elif menu == "Visual Learning Zone":

    st.title("Visual Learning Zone")
    st.subheader("Revision + Infographic Center")

    visual_unit = st.selectbox(
        "Select Visual Learning Topic",
        [
            "Political Map of Northeast India",
            "Ethnic Movements Timeline",
            "Autonomy Councils Structure",
            "Regional Political Movements",
            "Constitutional Framework of Northeast India",
            "Demographic Changes in Undivided Goalpara District"
        ]
    )

    if visual_unit == "Political Map of Northeast India":
        st.image("images/northeast_india_map.jpg", use_container_width=True)
        st.write("""
Important for understanding state formation, political boundaries,
strategic location, and regional identity politics.
""")

    elif visual_unit == "Ethnic Movements Timeline":
        st.image(
            load_visual_panel("ethnic_movements.png", "top_left"),
            use_container_width=True
        )
        st.write("""
Covers major ethnic assertions, identity movements, and autonomy demands
across Northeast India.
""")

    elif visual_unit == "Autonomy Councils Structure":
        st.image(
            load_visual_panel("autonomy_council.png", "top_right"),
            use_container_width=True
        )
        st.write("""
Explains Sixth Schedule areas, Autonomous District Councils,
and governance mechanisms.
""")

    elif visual_unit == "Regional Political Movements":
        st.image(
            load_visual_panel("regional_movements.png", "bottom_left"),
            use_container_width=True
        )
        st.write("""
Important student revision topic for regionalism, sub-nationalism,
and statehood movements.
""")

    elif visual_unit == "Constitutional Framework of Northeast India":
        st.image(
            load_visual_panel("constitutional_framework.png", "bottom_right"),
            use_container_width=True
        )
        st.write("""
Important for exams covering constitutional provisions,
special status, and federal structure.
""")
    elif visual_unit == "Demographic Changes in Undivided Goalpara District":

        st.image(
            "images/goalpara_demographic_changes.png",
            use_container_width=True
        )

    st.write("""
This visual explains the long-term demographic transformation of
Undivided Goalpara District from 1901 to 2020.

It helps students understand:

- migration and settlement patterns  
- religion and identity politics  
- demographic change and electoral politics  
- political implications of population shifts  
- regional tensions linked to migration debates

This is highly relevant for understanding Assam politics,
identity movements, and contemporary electoral discourse.
""") 
elif menu == "About & Disclaimer":

    st.title("About This Academic App")

    st.markdown("""
### POL060304 - Politics in Northeast India

This platform is developed for academic support of BA 6th Semester students.

### Academic Disclaimer

- This app is created strictly for educational purposes only.
- It is not an official university publication.
- Students must verify final academic guidance with faculty members and official syllabus.

### Credits

- Developed By: Nirban Ray
- Institution Support: B.P. Chaliha College
- Department: Political Science
- Course Code: POL060304
- Semester: BA 6th Semester
- Platform Version: v1.0

### Copyright Notice

- Content belongs to respective academic and educational sources and is in the developmental stage.
- Unauthorized commercial reproduction is prohibited.
- Educational fair use only.

### Feedback

For corrections, updates, or faculty review, please contact the department/admin.
""")

elif menu == "Faculty Admin":

    st.title("Faculty Admin")

    admin_password = st.text_input(
        "Enter Faculty Access Password",
        type="password"
    )

    if admin_password != FACULTY_PASSWORD:
        st.warning("Faculty access only.")
        st.stop()

    st.success("Access Granted")

    st.header("Faculty Admin Panel")
    st.warning("Only for faculty content updates")

    notes_data = load_notes_data()
    if not isinstance(notes_data, dict):
        notes_data = {}

    if st.session_state.pop("faculty_save_success", False):
        st.success("Note saved successfully")

    if st.session_state.pop("faculty_restore_success", False):
        st.success("Backup restored successfully")

    if st.session_state.pop("question_save_success", False):
        st.success("Question updated successfully.")

    unit_name = st.selectbox(
        "Select Unit",
        [
            "Unit I",
            "Unit II",
            "Unit III",
            "Unit IV"
        ],
        key="faculty_unit_name"
    )

    unit_topics = notes_data.get(unit_name, {})
    if not isinstance(unit_topics, dict):
        unit_topics = {}

    topic_options = list(unit_topics.keys()) + ["+ Add New Topic"]

    pending_topic_choice = st.session_state.pop(
        "faculty_pending_topic_choice",
        None
    )
    if pending_topic_choice in topic_options:
        st.session_state["faculty_topic_choice"] = pending_topic_choice

    topic_choice = st.selectbox(
        "Select Existing Topic",
        topic_options,
        key="faculty_topic_choice"
    )

    if topic_choice == "+ Add New Topic":
        if st.session_state.pop("faculty_clear_new_topic_name", False):
            st.session_state["faculty_new_topic_name"] = ""
        topic_name = st.text_input(
            "New Topic Name",
            key="faculty_new_topic_name"
        ).strip()
    else:
        topic_name = topic_choice

    editor_target = (unit_name, topic_choice)
    if st.session_state.get("faculty_editor_target") != editor_target:
        st.session_state["faculty_topic_content"] = (
            unit_topics.get(topic_name, "")
            if topic_choice != "+ Add New Topic"
            else ""
        )
        st.session_state["faculty_editor_target"] = editor_target

    topic_content = st.text_area(
        "Full Note Content",
        height=300,
        key="faculty_topic_content"
    )

    if st.button("Save Note"):

        if not topic_name:
            st.error("Enter a topic name before saving.")
        else:
            latest_notes_data = load_notes_data()
            if not isinstance(latest_notes_data, dict):
                latest_notes_data = {}

            latest_notes_data.setdefault(unit_name, {})
            latest_notes_data[unit_name][topic_name] = topic_content

            saved_data = save_notes_data(latest_notes_data)

            saved_content = saved_data.get(unit_name, {}).get(topic_name)

            if saved_content == topic_content:
                st.session_state["faculty_save_success"] = True
                st.session_state["faculty_pending_topic_choice"] = topic_name
                st.session_state["faculty_clear_new_topic_name"] = True
                st.session_state["faculty_editor_target"] = (unit_name, topic_name)
                st.rerun()
            else:
                st.error("Save verification failed. The JSON file did not update as expected.")

    st.markdown("---")
    st.subheader("Important Questions Editor")

    question_unit = st.selectbox(
        "Select Question Unit",
        list(important_questions.keys()),
        key="question_unit_select"
    )

    question_section = st.selectbox(
        "Select Section",
        list(important_questions[question_unit].keys()),
        key="question_section_select"
    )

    existing_questions = important_questions[question_unit][question_section]

    selected_question = st.selectbox(
        "Select Existing Question",
        ["Create New Question"] + existing_questions,
        key="question_existing_select"
    )

    if selected_question == "Create New Question":
        edited_question = st.text_area(
            "Enter New Question",
            height=150,
            key="new_question_editor"
        )
    else:
        edited_question = st.text_area(
            "Edit Selected Question",
            value=selected_question,
            height=150,
            key="existing_question_editor"
        )

    if st.button("Save Question Update"):

        normalized_question = edited_question.strip()

        if normalized_question:
            updated_questions = existing_questions.copy()

            if selected_question != "Create New Question":
                updated_questions.remove(selected_question)

            updated_questions.append(normalized_question)
            important_questions[question_unit][question_section] = updated_questions
            save_important_questions_data(important_questions)

            st.session_state["question_save_success"] = True
            st.rerun()

        else:
            st.error("Question cannot be empty.")

    st.markdown("---")
    st.subheader("✏️ Model Answers Editor")

    unit = st.selectbox(
            "Select Unit",
            list(model_answers_data.keys()),
            key="model_unit"
        )

    questions = model_answers_data[unit]

    question = st.selectbox(
        "Select Question",
        list(questions.keys()),
        key="model_question"
    )

    current_answer = questions[question]

    edited_answer = st.text_area(
        "Edit Answer",
        current_answer,
        height=200
    )

    if st.button("Save Model Answer"):
        model_answers_data[unit][question] = edited_answer
        save_model_answers(model_answers_data)
        st.success("Saved successfully")   

    st.markdown("---")
    st.subheader("✏️ Quick Revision Editor")

    selected_unit = st.selectbox(
        "Select Unit",
        list(quick_revision_data.keys()),
        key="edit_revision_unit"
    )

    current_items = quick_revision_data[selected_unit]

    edited_text = st.text_area(
        "Edit Revision (one point per line)",
        "\n".join(current_items),
        height=200
    )

    if st.button("Save Revision Update"):
        updated_list = [
            line.strip() for line in edited_text.split("\n") if line.strip()
        ]

        quick_revision_data[selected_unit] = updated_list

        from revision.quick_revision import save_quick_revision
        save_quick_revision(quick_revision_data)

        st.success("Saved successfully")   

    st.markdown("---")
    st.subheader("📊 Usage Analytics")

    df = pd.read_sql("SELECT * FROM usage", conn)

    if not df.empty:
            st.dataframe(df.tail(20))

            st.subheader("Most Viewed Topics")
            st.write(
                df.groupby("topic")
                .size()
                .sort_values(ascending=False)
                .head(10)
            )
    else:
            st.info("No analytics data yet")

    
    st.markdown("---")
    st.subheader("Backup System")

    with open(file_path, "r", encoding="utf-8") as f:
        backup_data = f.read()

    st.download_button(
        label="Download Full Backup",
        data=backup_data,
        file_name="notes_backup.json",
        mime="application/json"
    )

    st.markdown("---")
    st.subheader("Restore Backup")

    uploaded_backup = st.file_uploader(
        "Upload Backup JSON File",
        type=["json"],
        key="faculty_uploaded_backup"
    )

    if uploaded_backup is not None and st.button("Restore Backup"):

        restored_data = json.load(uploaded_backup)
        if not isinstance(restored_data, dict):
            st.error("Backup JSON must contain a top-level object.")
            st.stop()

        save_notes_data(restored_data)

        st.session_state["faculty_restore_success"] = True
        st.rerun()

        
# -----------------------------------
# FOOTER
# -----------------------------------


st.markdown("---")
st.caption(
    "Prepared and Maintained by\n"
    "Dr. Nirban Ray,\n"
    "Assistant Professor, Department of Political Science"
)
