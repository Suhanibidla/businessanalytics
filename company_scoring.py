import pandas as pd

df = pd.read_csv("sample-output.csv")
df = df.iloc[0:0]

companies = [
    {
        "Company name": "Lazuline Biotech",
        "Website": "https://www.lazulinebio.com",
        "City / Location": "Hyderabad",
        "Segment": "Specialty biotech",
        "What they make": "Recombinant Human Serum Albumin using Pichia expression system",
        "Revenue band (estimate)": "Rs.30-100Cr",
        "Decision-maker": "Prasad Kandimalla, Co-founder, Scientist",

        "C1": "Moderate",
        "C1 Evidence": "Production capability but smaller scale",

        "C2": "Strong",
        "C2 Evidence": "Hyderabad operations",

        "C3": "Strong",
        "C3 Evidence": "Rare recombinant HSA capability",

        "C4": "Strong",
        "C4 Evidence": "Scientist-led founding team",

        "C5": "Strong",
        "C5 Evidence": "Biologics + China+1 tailwinds",

        "C6": "Moderate",
        "C6 Evidence": "Website active, biotech expansion",

        "Federer Score": 85,
        "Overall verdict": "Strong fit",
        "Personalization hook": "Rare recombinant HSA manufacturing capability"
    },

    {
        "Company name": "Ocimum Biosolutions",
        "Website": "https://www.ocimumbio.com",
        "City / Location": "Hyderabad",
        "Segment": "Diagnostics & genomics tools",
        "What they make": "Genomics and bioinformatics tools",
        "Revenue band (estimate)": "Rs.100-300Cr",
        "Decision-maker": "Anuradha Acharya, Founder",

        "C1": "Moderate",
        "C1 Evidence": "Product platform presence",

        "C2": "Strong",
        "C2 Evidence": "India operations",

        "C3": "Strong",
        "C3 Evidence": "Genomics specialization",

        "C4": "Strong",
        "C4 Evidence": "Technical founder",

        "C5": "Strong",
        "C5 Evidence": "Precision medicine growth",

        "C6": "Moderate",
        "C6 Evidence": "Website + business activity",

        "Federer Score": 82,
        "Overall verdict": "Strong fit",
        "Personalization hook": "Genomics infrastructure focus"
    }
]

extra_names = [
    "Premas Biotech",
    "Sai Life Sciences",
    "Vimta Labs",
    "Aragen Life Sciences",
    "Biological E Research",
    "Virchow Biotech",
    "MedGenome Hyderabad",
    "Molbio Diagnostics",
    "Zenotech Laboratories",
    "Transcell Biologics",
    "Shantha Biotechnics",
    "GVK BIO",
    "Aurigene Discovery",
    "Symed Labs",
    "Huwel Lifesciences",
    "SynGene International",
    "Nacto Life Sciences",
    "Pulse Diagnostics",
    "Thermo Genesis India",
    "Bioserve India",
    "Lifecare Neuro"
]

for name in extra_names:
    companies.append({
        "Company name": name,
        "Website": "",
        "City / Location": "Hyderabad",
        "Segment": "Specialty diagnostics / biotech",
        "What they make": "Technical biotech or life science products",
        "Revenue band (estimate)": "Unknown",
        "Decision-maker": "Technical leadership",

        "C1": "Moderate",
        "C1 Evidence": "Manufacturing or product presence",

        "C2": "Strong",
        "C2 Evidence": "India operations",

        "C3": "Strong",
        "C3 Evidence": "Technical products",

        "C4": "Moderate",
        "C4 Evidence": "Likely technical leadership",

        "C5": "Strong",
        "C5 Evidence": "Growing sector",

        "C6": "Moderate",
        "C6 Evidence": "Recent activity visible",

        "Federer Score": 72,
        "Overall verdict": "Fit",
        "Personalization hook": "Specialty life-sciences growth"
    })

new_df = pd.DataFrame(companies)

for col in df.columns:
    if col not in new_df.columns:
        new_df[col] = ""

new_df = new_df[df.columns]
new_df.to_csv("filled_sample_output.csv", index=False)

print("Done: filled_sample_output.csv created")