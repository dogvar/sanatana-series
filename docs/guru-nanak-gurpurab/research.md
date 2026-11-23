# Guru Nanak Dev Ji Gurpurab 2026: research and source notes

Checked 21 November 2026. Starting commit: `d1e9d23`. These notes are for editors and are not reader-facing.

## Date evidence

| Fact | Finding | Source | Status |
|---|---|---|---|
| 2026 observance | Tuesday, 24 November 2026, Kartik Purnima | Office Holidays (Punjab); Wikipedia, Guru Nanak Gurpurab; repository calendar lists Kartik Purnima on the same date | Confirmed by secondary sources |
| Anniversary | 557th (2026 − 1469). All India Radio called 2025 the 556th | newsonair.gov.in | Confirmed |
| Drik Panchang city listing | Page returned HTTP 403 | n/a | **Not checked** |
| Birth month | Kartik in the Bala tradition and in the observance; Vaisakh (April 1469) in most Janamsakhis and for many historians | Wikipedia, Guru Nanak | Disputed, stated in Chapter 1 |

The guide gives no clock times for 2026. It sends readers to their local gurdwara.

## Gurbani verification

Every line was compared programmatically with the BaniDB API (`api.banidb.com/v2/angs/{ang}/G`). Gurmukhi, Latin transliteration, Devanagari transliteration and author matched exactly in both editions.

| Line | Ang | Bani | Author in BaniDB | Use |
|---|---|---|---|---|
| ੴ ਸਤਿ ਨਾਮੁ … ਗੁਰ ਪ੍ਰਸਾਦਿ ॥ | 1 | Mul Mantar | Guru Nanak Dev Ji | Quoted |
| ਘਾਲਿ ਖਾਇ ਕਿਛੁ ਹਥਹੁ ਦੇਇ ॥ ਨਾਨਕ ਰਾਹੁ ਪਛਾਣਹਿ ਸੇਇ ॥੧॥ | 1245 | Sarang ki Var, salok | Guru Nanak Dev Ji | Quoted |
| ਸੋ ਕਿਉ ਮੰਦਾ ਆਖੀਐ ਜਿਤੁ ਜੰਮਹਿ ਰਾਜਾਨ ॥ | 473 | Asa di Var, salok | Guru Nanak Dev Ji | Quoted |
| ਸਚਹੁ ਓਰੈ ਸਭੁ ਕੋ ਉਪਰਿ ਸਚੁ ਆਚਾਰੁ ॥੫॥ | 62 | Sri Raag | Guru Nanak Dev Ji | Paraphrased |
| ਦਇਆ ਕਪਾਹ ਸੰਤੋਖੁ ਸੂਤੁ ਜਤੁ ਗੰਢੀ ਸਤੁ ਵਟੁ ॥ | 471 | Asa di Var | Guru Nanak Dev Ji | Paraphrased |
| ਜੈਸੀ ਮੈ ਆਵੈ ਖਸਮ ਕੀ ਬਾਣੀ … ਵੇ ਲਾਲੋ ॥ and ਪਾਪ ਕੀ ਜੰਞ ਲੈ ਕਾਬਲਹੁ ਧਾਇਆ … | 722 | Tilang | Guru Nanak Dev Ji | Referenced, same shabad |

Translations: English follows BaniDB's default translation. Hindi is based on BaniDB's Sahib Singh Hindi text, lightly normalised for punctuation and readability. A Gurbani-literate reviewer should approve both, including the gendered wording in the English ("God", "he").

## Classification of major claims

| Claim | Category | Basis |
|---|---|---|
| Birth 1469, Talwandi; parents; sister; wife; sons | Historical/traditional consensus | Wikipedia with references |
| Sultanpur, modikhana, Jai Ram, Daulat Khan | Traditional, widely accepted | Wikipedia, Guru Nanak and Bebe Nanaki |
| Janeu refusal | Janamsakhi tradition | Widely told. **Recension not verified.** The priest is left unnamed. The linked verse (Ang 471) is verified |
| Sacha Sauda | Janamsakhi tradition | Secondary retellings. **Recension not verified.** Age and companion vary, and the guide says so |
| Bein River, three days, "no Hindu, no Muslim" | Sikh tradition/Janamsakhi | Wikipedia, Britannica search summary. Saying is not presented as Gurbani |
| Four Udasis and destinations | Tradition, routes disputed | Wikipedia. Labelled in the guide |
| Lalo and Malik Bhago, milk and blood | Janamsakhi tradition | Secondary retellings. Lalo's address in Gurbani is verified at Ang 722 |
| Haridwar and Mecca stories | Janamsakhi tradition | Secondary retellings |
| Kartarpur, farming, langar, sangat | Historical core with traditional detail | Wikipedia; founding year disputed (1504, 1515 and 1522 appear), so the guide gives none in prose |
| Succession of Angad, death September 1539 | Historical | Wikipedia. 22 September is the usual conversion |
| Flowers at death | Tradition | Labelled in the guide |
| Adi Granth 1604; Guruship 1708 | Historical | Wikipedia, Guru Granth Sahib |
| 1,430 Angs; Guru Nanak's 974 hymns | Standard counts | Wikipedia. The guide says "close to a thousand" |
| Gurpurab observances | Community practice | Wikipedia, Guru Nanak Gurpurab; Nagar kirtan; Akhand Path |

## Sources that could not be read

- **SGPC Sikh Rehat Maryada:** the English PDF exceeded the fetch tool's size limit. The gurdwara etiquette paragraph links to it but **has not been checked line by line against it**.
- **Britannica:** blocked (403). Only a search summary was seen.
- **SikhiWiki:** blocked (403). Only search summaries were seen.
- **Drik Panchang:** blocked (403).
- **Puratan, Bala and Miharban Janamsakhi editions, McLeod, Grewal, Harbans Singh:** not consulted directly. Wikipedia is carrying more weight than the brief's preferred sources, and a Sikh studies reviewer should check the narrative chapters.

## Editorial decisions

- No invented dialogue. Reported speech follows the traditional outline and is labelled.
- "Sikhi", "Gurbani", "Ang", "Parkash" and "Ardas" are used instead of Hindu equivalents. The Hindi avoids "जयंती".
- The story of the Panj Pyare notes that they date from 1699, after Guru Nanak.
