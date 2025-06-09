import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objects as go
import streamlit.components.v1 as components
st.set_page_config(
    page_title="Your doctor",
    layout="wide"
)
with st.sidebar:
  selected = option_menu(
        menu_title=None,
        options = ["Chat","Dashboard"]
  )
  st.subheader("Add files")
  d = st.file_uploader(label=" ",type=["csv","xlsx"])
  
if selected == "Dashboard":
   data = pd.read_csv(d)
   data = data.dropna()
   col1, col2, col3, col4, col5 = st.columns(5)
   col6,col7,col8 = st.columns(3)
   with col1:
     drop = st.selectbox(label="Patient's Vital Status",options=["living","dead"])
   if drop == "living":
     data_liv = data[data["Patient's Vital Status"] =="Living"]
     li = len(data_liv)
     data_liv["Hormone Therapy"].value_counts()
     li1 = len(data_liv[data_liv["Hormone Therapy"]=="Yes"])
     li2 = len(data_liv[data_liv["Chemotherapy"]=="Yes"])
     li3 = len(data_liv[data_liv["Radio Therapy"]=="Yes"])
     data_liv["HER2 status measured by SNP6"].value_counts()
     data11 = pd.DataFrame({"HER2 status":data_liv["HER2 status measured by SNP6"].value_counts().index,"values":data_liv["HER2 status measured by SNP6"].value_counts().values})
     data25 = data_liv[["Patient ID","Mutation Count","Cellularity","Pam50 + Claudin-low subtype","Overall Survival (Months)","Relapse Free Status (Months)"]]
     data23 = data_liv[["Patient ID","Integrative Cluster","Nottingham prognostic index","Oncotree Code","Lymph nodes examined positive"]]
     prog1 = []
     for i in data23.index:
       x = data23.loc[i,"Nottingham prognostic index"]
       if x < 2.4:
         prog1.append("excellent")
       elif 2.4 <= x <= 3.4:
         prog1.append("good")
       elif 3.41 <= x <= 5.4:
         prog1.append("intermediate")
       else:
         prog1.append("poor")
     data23["prognosis"] = prog1
     data23["prognosis"].value_counts()
     data_liv["Oncotree Code"].value_counts()
     data10 = pd.DataFrame({"Oncotree Code":data_liv["Oncotree Code"].value_counts().index,"values":data_liv["Oncotree Code"].value_counts().values})
     cluster1 = data_liv["Integrative Cluster"].value_counts()
     #data_cluster1 = pd.DataFrame({"IC":cluster1.index,"values":cluster1.values,"prognosis":prog})
     data_cluster1 = pd.DataFrame({"clusters":["IC1","IC2","IC3","IC4","IC5","IC6","IC7","IC8","IC9","IC10","4ER-"],
                      "values":[37,14,80,74,33,19,51,64,29,65,18],
                      "prognosis":["Intermediate","Poor","Good","Excellent","Poor","Intermediate","Intermediate","Very poor","Poor","Very poor","Poor"]})
     data44 = pd.DataFrame({"prognosis":data23["prognosis"].value_counts().index,"values":data23["prognosis"].value_counts().values})
     col2.metric("Living patients",value=li)
     col3.metric("Hormone Therapy patients",value=li1)
     col4.metric("Chemotherapy patients",value=li2)
     col5.metric("Radiotherapy patients",value=li3)
     style_metric_cards(background_color="green",         # Entire card background
          border_left_color="green",border_color="green")
     with col6:
        st.subheader("HER2 status")
        fig1 = go.Figure(go.Pie(labels=data11["HER2 status"],values=data11["values"],hole=0.5))
        fig1.update_layout(width=260,height=180,margin=dict(t=20, b=0, l=0, r=0),legend=dict(
        x=1,          # move legend horizontally (0 = left, 1 = right)
        y=1,          # move legend vertically (0 = bottom, 1 = top)
        xanchor='left', # anchor legend position
        yanchor='middle',
        orientation='v',
        font=dict(size=12),
        ))
        st.plotly_chart(fig1, use_container_width=True)
        st.subheader("Prognosis")
        f1 = px.bar(data44,x="prognosis",y="values",color="prognosis")
        f1.update_layout(height=200,margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(f1,use_container_width=False)
     with col7:
        st.subheader("Relapse Free Status")
        f2 = px.scatter(data25,x="Relapse Free Status (Months)",y="Mutation Count",color="Cellularity",hover_data=["Patient ID","Pam50 + Claudin-low subtype"])
        f2.update_traces(marker=dict(size=10))
        f2.update_layout(width=1500,height=200,margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(f2,use_container_width=False)
        st.subheader("Oncocode Tree")
        fig2 = px.area(data10,x="Oncotree Code",y="values")
        fig2.update_layout(height=200,margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig2,use_container_width=False)
     with col8:
        st.subheader("Integrative Clusters")
        f2 = px.bar(data_cluster1,x="values",y="clusters",color="prognosis", orientation='h')
        f2.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(f2,use_container_width=False)
     
     
   if drop == "dead":
     data_liv = data[data["Patient's Vital Status"] =="Died of Disease"]
     li = len(data_liv)
     data_liv["Hormone Therapy"].value_counts()
     data11 = pd.DataFrame({"HER2 status":data_liv["HER2 status measured by SNP6"].value_counts().index,"values":data_liv["HER2 status measured by SNP6"].value_counts().values})
     data25 = data_liv[["Patient ID","Mutation Count","Cellularity","Pam50 + Claudin-low subtype","Overall Survival (Months)","Relapse Free Status (Months)"]]
     data23 = data_liv[["Patient ID","Integrative Cluster","Nottingham prognostic index","Oncotree Code","Lymph nodes examined positive"]]
     prog1 = []
     for i in data23.index:
       x = data23.loc[i,"Nottingham prognostic index"]
       if x < 2.4:
         prog1.append("excellent")
       elif 2.4 <= x <= 3.4:
         prog1.append("good")
       elif 3.41 <= x <= 5.4:
         prog1.append("intermediate")
       else:
         prog1.append("poor")
     data23["prognosis"] = prog1
     data23["prognosis"].value_counts()
     data_liv["Oncotree Code"].value_counts()
     data10 = pd.DataFrame({"Oncotree Code":data_liv["Oncotree Code"].value_counts().index,"values":data_liv["Oncotree Code"].value_counts().values})
     data_cluster1 = pd.DataFrame({"clusters":["IC1","IC2","IC3","IC4","IC5","IC6","IC7","IC8","IC9","IC10","4ER-"],
                      "values":[26,23,33,42,65,23,30,43,32,38,15],
                      "prognosis":["Intermediate","Poor","Good","Excellent","Poor","Intermediate","Intermediate","Very poor","Poor","Very poor","Poor"]})
     data44 = pd.DataFrame({"prognosis":data23["prognosis"].value_counts().index,"values":data23["prognosis"].value_counts().values})
     li1 = len(data_liv[data_liv["Hormone Therapy"]=="Yes"])
     li2 = len(data_liv[data_liv["Chemotherapy"]=="Yes"])
     li3 = len(data_liv[data_liv["Radio Therapy"]=="Yes"])
     col2.metric("Patients died",value=li)
     col3.metric("Hormone Therapy patients",value=li1)
     col4.metric("Chemotherapy patients",value=li2)
     col5.metric("Radiotherapy patients",value=li3)
     style_metric_cards(background_color="red",         # Entire card background
          border_left_color="red",border_color="red")
     with col6:
        st.subheader("HER2 status")
        fig1 = go.Figure(go.Pie(labels=data11["HER2 status"],values=data11["values"],hole=0.5))
        fig1.update_layout(width=260,height=180,margin=dict(t=20, b=0, l=30, r=20),legend=dict(
        x=1,          # move legend horizontally (0 = left, 1 = right)
        y=1,          # move legend vertically (0 = bottom, 1 = top)
        xanchor='left', # anchor legend position
        yanchor='middle',
        orientation='v',
        font=dict(size=12),
        ))
        st.plotly_chart(fig1,use_container_width=False)
        st.subheader("Prognosis")
        f1 = px.bar(data44,x="prognosis",y="values",color="prognosis")
        f1.update_layout(height=200,margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(f1,use_container_width=False)
     with col7:
        st.subheader("Relapse Free Status")
        f2 = px.scatter(data25,x="Relapse Free Status (Months)",y="Mutation Count",color="Cellularity",hover_data=["Patient ID","Pam50 + Claudin-low subtype"])
        f2.update_traces(marker=dict(size=10))
        f2.update_layout(width=1500,height=200,margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(f2,use_container_width=False)
        st.subheader("Oncocode Tree")
        fig2 = px.area(data10,x="Oncotree Code",y="values")
        fig2.update_layout(height=200,margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig2,use_container_width=False)
     with col8:
        st.subheader("Integrative Clusters")
        f2 = px.bar(data_cluster1,x="values",y="clusters",color="prognosis", orientation='h')
        f2.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(f2,use_container_width=False)

if selected == "Chat":
  st.title("Your Doctor")
  st.subheader("Hey! I am your doctor. How can I help you?")
  t1 = st.text_input("enter any queries")
  if "mastectomy" in t1:
    st.write("A mastectomy is a surgical procedure where breast tissue is removed. It's often performed to treat breast cancer but can also be used to prevent cancer in individuals with a high risk. There are different types of mastectomies, including simple (total) mastectomy, where the entire breast is removed, and nipple-sparing or skin-sparing mastectomies, which preserve specific areas of the breast for reconstructive purposes. ")
    st.write("🔍 Types of Mastectomy:")
    st.write("1. Simple (Total) Mastectomy: Removal of the entire breast, but not the lymph nodes under the arm or the muscle beneath the breast.")
    st.write("2. Modified Radical Mastectomy: Removal of the entire breast along with axillary (underarm) lymph nodes.")
    st.write("3. Radical Mastectomy: Removal of the entire breast, lymph nodes, and chest wall muscles (rarely done now).")
    st.write("4. Skin-Sparing Mastectomy: The breast tissue is removed, but most of the skin over the breast is saved.")
    st.write("5. Nipple-Sparing Mastectomy: The breast tissue is removed but the nipple and skin are preserved (used in select cases).")
  if "breast conserving" in t1:
    st.write("Breast conserving, usually refers to breast-conserving surgery (BCS), also known as a lumpectomy or partial mastectomy. This is a treatment option for breast cancer where only the tumor and a small margin of surrounding tissue are removed, rather than the entire breast (as in a mastectomy).")
    st.write("💥 Key Points:")
    st.write("1. Goal: To remove the cancer while retaining as much of the natural breast as possible.")
    st.write("2. Often followed by radiation therapy: To kill any remaining cancer cells and reduce the risk of recurrence.")
    st.write("3. Suitable for: Early-stage breast cancer or localized tumors.")
    st.write("4. Benefits: Preserves breast appearance and sensation to a greater extent than mastectomy.")
  if "chemotherapy" in t1:
    st.write("Chemotherapy is a type of cancer treatment that uses drugs to kill cancer cells. It's one of the most common forms of systemic cancer therapy, meaning it works throughout the entire body, not just at the site of a tumor.")
    st.write("💥 Key Points:")
    st.write("1. Targets fast-growing cells, which includes cancer cells. Unfortunately, it also affects some healthy fast-growing cells (like those in hair follicles, bone marrow, and the digestive tract), which leads to side effects.")
    st.write("2. It is given most commonly directly in bloodstream, also be given in the form of pills, cream or by injections.")
    st.write("3. Given in cycles, depending on type and stage of cancer and how well the patient responds.")
    st.write("4. Short term side effects: Fatigue, nausea, vomiting, hair loss, loss of appetite, low blood cell counts.")
    st.write("5. Can sometimes cause lasting damage to the heart, kidneys, lungs, or nerves.")
  if ("invasive ductal carcinoma" in t1) or ("idc" in t1):
    st.write(f"Invasive Ductal Carcinoma (IDC) is the most common type of breast cancer, accounting for about 70–80% of all breast cancer cases. It starts in the milk ducts of the breast and invades the surrounding breast tissue. Invasive, means the cancer has spread beyond the ducts into nearby tissue, and it can potentially metastasize (spread) to other parts of the body.")
    st.write("⚠️ Common signs and symptoms include:")
    st.write("1. A lump in the breast or underarm.")
    st.write("2. Change in breast shape or size.")
    st.write("3. Nipple discharge (possibly bloody).")
    st.write("4. Pain in the breast or nipple.")
    st.write("🧪 Diagnosis usually involves:")
    st.write("1. Physical examination.")
    st.write("2. Imaging tests: Mammogram, ultrasound, MRI.")
    st.write("3. Biopsy: Core needle biopsy or fine needle aspiration.")
    st.write("4. Pathology tests: To determine hormone receptor status (ER, PR) and HER2 status.")

  if ("lobular carcinoma" in t1):
    st.write(f"Lobular carcinoma refers to a type of breast cancer that begins in the lobules, which are the glands in the breast responsible for producing milk. It is one of the two main types of invasive breast cancer, the other being ductal carcinoma, which starts in the milk ducts.")
    st.write("🔍 Types:")
    st.write("Lobular Carcinoma In Situ (LCIS):")
    st.write("It is not cancer, but a marker indicating increased risk of developing breast cancer in the future. Found incidentally during a biopsy for another reason. Usually does not form a lump or show up on a mammogram.")
    st.write("Invasive Lobular Carcinoma (ILC):")
    st.write(f"Cancerous and can spread to surrounding tissues and other parts of the body. Typically grows in a single-file pattern, making it harder to detect on imaging. Represents about 10–15% of all invasive breast cancers.")
    st.write("⚠️ Common signs and symptoms include:")
    st.write("1. A thickening or hardening in the breast rather than a distinct lump.")
    st.write("2. Changes in breast texture or fullness.")
    st.write("🧪 Diagnosis:")
    st.write("1. Mammogram and ultrasound (may be less sensitive for ILC).")
    st.write("2. MRI may be more effective due to the diffuse growth pattern.")
  
  if ("invasive breast carcinoma" in t1) or ("ibc" in t1):
    st.write(f"Mucinous carcinoma is a rare type of cancer that produces mucin — the main component of mucus. This type of cancer can occur in various organs but is most commonly found in the breast, colon, rectum, pancreas, and ovaries.")
    st.write("Key Features:")
    st.write("🔬 Histology:")
    st.write("Tumors contain pools of mucin in which cancer cells are found floating. Appears gelatinous on gross pathology.")
    st.write("🔍 Types:")
    st.write("Pure mucinous carcinoma: Composed almost entirely of mucin-producing cancer cells.")
    st.write("Mixed mucinous carcinoma: Contains both mucinous and other types of cancer cells (e.g., ductal carcinoma in the breast).")
    st.write("⚠️ Symptoms:")
    st.write("Depend on the site but may include lumps (breast), abdominal pain (GI tract), bloating (ovary), or changes in bowel habits (colon).")
    st.write("🧪 Diagnosis:")
    st.write("Imaging (e.g., mammography, CT, MRI), Biopsy, histopathology and Immunohistochemistry")

  if ("breast angiosarcoma" in t1):
    st.write(f"Breast angiosarcoma is a rare and aggressive form of cancer that originates in the blood or lymphatic vessels of the breast. It accounts for less than 0.05% of all breast malignancies.")
    st.write("🔍 There are two main types:")
    st.write("Primary breast angiosarcoma:")
    st.write("Occurs de novo (on its own), usually in younger women (20–40 years). Not associated with prior cancer or treatment. ")
    st.write("Secondary breast angiosarcoma:")
    st.write(f"Develops as a complication of radiation therapy or chronic lymphedema. Typically affects older women who were previously treated for breast cancer. Usually appears 5–10 years after radiation therapy.")
    st.write("⚠️ Symptoms:")
    st.write("1. A rapidly growing, painless mass in the breast.")
    st.write("2. Skin discoloration (blue-purple or red hue).")
    st.write("3. Swelling or skin thickening.")
    st.write("4. Sometimes ulceration or bleeding.")
    st.write("🧪 Diagnosis:")
    st.write("1. Imaging: Mammography, ultrasound, and especially MRI.")
    st.write("2. Biopsy: Core needle or surgical biopsy to confirm histology.")
    st.write("3. Histopathology: Shows irregular vascular channels, high mitotic rate, and atypical endothelial cells.")

  if ("metaplastic breast cancer" in t1) or ("mpbc" in t1):
    st.write(f"Metaplastic Breast Cancer (MpBC) is a rare and aggressive subtype of breast cancer, accounting for less than 1% of all breast cancer cases. It is distinct from more common forms like invasive ductal carcinoma due to its unique pathology, behavior, and resistance to standard therapies.")
    st.write("⚠️ Clinical Features:")
    st.write("1. Aggressive tumor growth")
    st.write("2. Larger tumor size at diagnosis")
    st.write("3. Higher risk of recurrence and metastasis, especially to lungs and bones")
    st.write("4. Common in women over 50, but can occur at younger ages")
    st.write("🧪 Diagnosis:")
    st.write("1. Requires histopathological analysis and immunohistochemistry.")
    st.write("2. Can mimic other tumors (e.g., sarcomas or squamous cell carcinomas).")
    st.write("3. Often diagnosed later due to atypical imaging characteristics.")

  if ("radiotherapy" in t1) or ("radio therapy" in t1):
    st.write(f"Radiotherapy (or radiation therapy) is a medical treatment that uses high doses of radiation to kill cancer cells or shrink tumors. It’s one of the most common treatments for cancer, often used alongside surgery or chemotherapy.")
    st.write("🔬 How it works:")
    st.write("Radiation damages the DNA of cancer cells, making them unable to grow and divide. Healthy cells can also be affected, but they usually recover better than cancer cells.")
    st.write("🩺 Common Uses:")
    st.write("- Brain tumors")
    st.write(f"- Breast cancer")
    st.write("- Prostate cancer")
    st.write("- Head and neck cancers")
    st.write("- Lung cancer")
    st.write("⚠️ Side Effects (vary depending on treatment site):")
    st.write("1. Fatigue")
    st.write("2. Skin irritation (like sunburn).")
    st.write("3. Hair loss (only in treated area).")
    st.write("4. Nausea or digestive issues.")
    st.write("5. Long-term: fibrosis, secondary cancers (rare)")
    st.write("✅ Benefits:")
    st.write("1. Can cure or control cancer.")
    st.write("2. Can relieve symptoms (palliative radiotherapy).")
    st.write("3. Often non-invasive and outpatient-based.")

  if ("luminal A claudin low subtype" in t1) or ("lum A" in t1):
    st.write(f"The Luminal A and Claudin-low subtypes are molecular classifications of breast cancer that differ significantly in terms of biology, prognosis, and treatment response. Here’s a breakdown of each and their relevance:")
    st.write("1. Hormone receptor status: Estrogen receptor-positive (ER+), Progesterone receptor-positive (PR+)")
    st.write("2. HER2: Negative")
    st.write("3. Ki-67 (proliferation marker): Low")
    st.write("4. Gene expression profile: High expression of luminal genes (e.g., ESR1, GATA3)")
    st.write("5. Prognosis: Best prognosis among breast cancer subtypes")
    st.write("🩺 Treatment:")
    st.write("Responds well to hormone therapy (e.g., tamoxifen, aromatase inhibitors); chemotherapy may not be needed")

  if ("luminal B claudin low subtype" in t1) or ("lum B" in t1):
    st.write(f"The term Luminal B Claudin-low subtype refers to a rare or hybrid molecular profile found in breast cancer. To understand it properly, let's break down both components:")
    st.write("1. Hormone receptor status: Usually Estrogen receptor-positive (ER+)")
    st.write("2. HER2: Typically HER2-negative or HER2-positive, with higher proliferation (Ki-67 index) compared to Luminal A.")
    st.write("3. More aggressive than Luminal A.")
    st.write("🩺 Treatment:")
    st.write("Often responsive to endocrine therapy, but may also need chemotherapy.")

  if ("HER2 claudin low subtype" in t1) or ("HER2 subtype" in t1):
    st.write(f"The HER2 claudin-low subtype of breast cancer is a specific type characterized by low expression of the HER2 protein and the claudin proteins, along with certain other molecular features. It's important to note that it's not a simple subtype but rather a complex phenotype that can occur across different intrinsic breast cancer subtypes.")
    st.write("🔬 Clinical Implications:")
    st.write("1. Poor prognosis: Claudin-low tumors are often associated with a poor prognosis, with high recurrence rates and a tendency to metastasize.")
    st.write("2. Limited response to standard therapies: They may not respond well to standard chemotherapy regimens, especially those targeting HER2-positive tumors.")
    st.write("3. Emerging treatment strategies: Research is ongoing to identify new targeted therapies and treatment strategies for claudin-low breast cancer.")
    st.write("4. Importance of personalized treatment: The heterogeneity of claudin-low tumors suggests that personalized treatment approaches based on the specific molecular characteristics of each tumor may be necessary.")

  if ("basal like claudin low subtype" in t1) or ("basal" in t1):
    st.write(f"Triple-negative breast cancer (TNBC) is an aggressive subtype of breast cancer where the tumor cells lack estrogen and progesterone receptors, and do not overexpress the HER2 protein. This lack of these receptors means that hormone therapies and targeted therapies that target HER2 are not effective, making chemotherapy the primary systemic treatment option. TNBC is typically diagnosed through a biopsy, where cells are analyzed for the presence or absence of these receptors.")
    st.write("🔬 Key Characteristics and Treatment:")
    st.write("⚠️ Aggressive Nature:")
    st.write("  TNBC tends to grow and spread faster than other breast cancer subtypes, often leading to metastasis and recurrence.")
    st.write("🩺 Treatment Focus:")
    st.write("  Chemotherapy is the primary systemic treatment, often used in combination with surgery and radiation therapy.")
    st.write("🧪 Emerging Therapies:")
    st.write("  Immunotherapy, such as checkpoint inhibitors, is showing promise in treating TNBC, particularly when combined with chemotherapy.")

  if ("ER status" in t1):
    st.write(f"ER status in the context of breast cancer refers to whether a tumor has estrogen receptors. These receptors are proteins found on the surface of some breast cancer cells that can bind to estrogen, a hormone that can stimulate cancer cell growth. Breast cancers are categorized as ER-positive or ER-negative based on this receptor status, which helps determine treatment options.")
    st.write("🔍 Classifications:")
    st.write("1. ER-positive breast cancer:")
    st.write("  These cancers have estrogen receptors. Hormone therapies, like tamoxifen, can block estrogen from binding to the receptors, slowing or stopping cancer growth.")
    st.write("2. ER-negative breast cancer:")
    st.write("  These cancers do not have estrogen receptors. Hormone therapies are not effective for these cancers, and other treatment options are needed.")

  if ("PR status" in t1):
    st.write(f"PR (progesterone receptor) status refers to whether the cancer cells have progesterone receptors. A PR-positive breast cancer means the cancer cells have these receptors, while a PR-negative cancer does not. This status is important for determining the effectiveness of certain treatments, particularly endocrine therapy, which works by blocking the effects of hormones like progesterone.")
    st.write("🔍 Classifications:")
    st.write("1. PR-positive breast cancer:")
    st.write("  If the cancer cells have progesterone receptors, they are considered PR-positive. This means the cancer cells can respond to the hormone progesterone.")
    st.write("2. PR-negative breast cancer:")
    st.write("  If the cancer cells do not have progesterone receptors, they are considered PR-negative. This means the cancer cells are not influenced by progesterone in the same way.")
    
  if ("hormone therapy" in t1):
    st.write(f"Hormone therapy refers to the medical use of hormones or hormone-blocking drugs to treat various conditions. In breast cancer it is used to block estrogen (in hormone receptor-positive cancers).")
    st.write("🔬 Common drugs:")
    st.write("Tamoxifen, aromatase inhibitors (like anastrozole, letrozole).")
    st.write("⚠️ Possible Side Effects:")
    st.write("Blood clots, stroke, increased cancer risks (in some forms), mood changes, etc.")
    st.write("❌ Not suitable for:")
    st.write("Individuals with a history of certain cancers, blood clots, liver disease, etc.")

  if ("HER2 status" in t1):
    st.write(f"HER2 status in breast cancer refers to whether a breast cancer tumor has excessive levels of the human epidermal growth factor receptor 2 (HER2) protein. HER2 is a protein that helps regulate cell growth and division, and in breast cancer, it can be overexpressed or amplified, leading to faster growth and spread.")
    st.write("🔍 Classifications:")
    st.write("1. HER2-Positive Breast Cancer:")
    st.write(" - Definition: Breast cancer cells with higher-than-normal HER2 protein levels or gene amplification. ")
    st.write(" 🔬 Characteristics: These cancers tend to grow and spread faster than HER2-negative breast cancers.")
    st.write(" 🩺 Treatment: HER2-positive breast cancers often respond well to targeted therapies that block the HER2 protein, such as trastuzumab (Herceptin).")
    st.write("2. HER2-Negative Breast Cancer:")
    st.write(" - Definition: Breast cancer cells with normal levels of HER2 protein expression and no gene amplification. ")
    st.write(" 🔬 Characteristics: These cancers are typically treated based on their hormone receptor status and other factors.")
    st.write(" 🩺 Treatment: HER2-targeted therapies are not beneficial for HER2-negative breast cancer.")

  if ("integrative clusters" in t1) or ("clusters" in t1) :
    st.write("Integrative Cluster (IntClust) subtypes in breast cancer provide a framework for classifying tumors based on both copy number and gene expression. This classification helps identify distinct groups of breast cancers with unique biological drivers, prognoses, and potential responses to treatment. IntClusts are based on the analysis of genomic and expression data, allowing for a more detailed understanding of breast cancer heterogeneity. Here's a more detailed breakdown:")
    st.subheader("🧬 Quick Overview of Integrative Clusters")
    table = pd.DataFrame({"clusters":["IC1","IC2","IC3","IC4","IC5","IC6","IC7","IC8","IC9","IC10"],
                      "Key features":["11q13/14 amplification (includes CCND1)","17q12 amplification (includes ERBB2/HER2)","16q deletion, low proliferation","Genomically stable","	8q amplification","16p gain","8p loss, 11q gain","Complex rearrangements, TP53 mutations","1q gain, 16q loss","BRCA1 mutation-like profile"],
                      "Associated subtypes":["Luminal B","HER2 enriched","Luminal A","Luminal A","Basal-like (Triple-negative)","Luminal B","Luminal A/B","Basal-like","Luminal B","Basal-like (Triple-negative)"],
                      "Prognosis":["Intermediate","Poor","Good","Excellent","Poor","Intermediate","Intermediate","Very poor","Poor","Very poor"]})
    table
  if ("mutations" in t1):
    st.write(f"Mutations, or changes, in certain genes can significantly increase the risk of developing breast cancer. These mutations can be inherited (germline mutations) or occur during a person's lifetime (somatic mutations). The most well-known examples are mutations in the BRCA1 and BRCA2 genes, which are tumor suppressor genes, meaning they normally help repair damaged DNA.")
    st.write("📝 Description:")
    st.write(f"1. HER2-Positive Breast Cancer: Mutations in BRCA1 or BRCA2 are inherited from a parent and are responsible for about 5-10% of breast cancer cases.")
    st.write("2. Increased Risk: Individuals with inherited BRCA1 or BRCA2 mutations have a significantly higher lifetime risk of developing breast cancer compared to the general population.")
    st.write("3. Other Cancers: These mutations also increase the risk of other cancers, including ovarian, pancreatic, prostate, and melanoma.")
    st.write("4. Autosomal Dominant Inheritance: BRCA1 and BRCA2 mutations are inherited in an autosomal dominant pattern, meaning one mutated copy of the gene is sufficient to increase cancer risk.")

  if ("npi" in t1) or ("NPI" in t1) or ("Nottingham Prognostic Index" in t1):
    st.write(f"The Nottingham Prognostic Index (NPI) is a tool used in breast cancer treatment to predict prognosis and guide treatment decisions. It combines tumor size, lymph node involvement, and tumor grade into a single score, which helps categorize patients into different prognostic groups.")
    st.write("Purpose:")
    st.write(f"The NPI is primarily used to determine the likelihood of a breast cancer patient's survival and to help decide whether or not to recommend adjuvant chemotherapy.")
    st.write("Calculation")
    st.write(f"The NPI is calculated by adding the values of tumor size (cm) multiplied by a coefficient of 0.2, the number of involved lymph nodes (0-3 points), and the histological grade (1-3 points).")
    st.write("Prognostic Groups:")
    st.write(f"Patients are typically categorized into good, moderate, and poor prognostic groups based on their NPI score.")
    st.subheader("Quick Overview of Nottingham Prognostic Index")
    table1 = pd.DataFrame({"score":["less than 2.4","Between 2.41 to 3.4","Between 3.41 to 5.4","greater than 5.4"],"prognosis":["excellent","good","moderate","poor"]})
    table1

  if ("nhg" in t1) or ("NHG" in t1) or ("neoplasm histologic grade" in t1):
    st.write(f"Histologic grading of a neoplasm refers to a description of a tumor based on how abnormal the cancer cells and tissue look under a microscope. It helps determine how quickly cancer cells are likely to grow and spread. Low-grade tumors, where cells resemble normal cells, tend to grow and spread more slowly than high-grade tumors, where cells look very different. Histologic grading is a way to classify a tumor based on the degree of differentiation, which means how much the cancer cells resemble the normal cells of the tissue where the tumor originated.")
    st.write("🔍 How is it done?")
    st.write(f"1. Microscopic Examination: Pathologists examine the tumor cells under a microscope.")
    st.write(f"2. Assessment of Cellular Features: They look at various features, including cell size, shape, and structure, as well as the arrangement of cells within the tumor.")
    st.write(f"3. Grading System: The assessment is then used to assign a grade, usually on a scale of 1 to 4, with 1 being the lowest (well-differentiated) and 4 being the highest (poorly differentiated).")

  if ("prognosis" in t1):
    st.write("Prognosis means the expected outcome or future course of a disease — how likely a person is to recover, how fast it may grow or spread, and what the chances of survival are. In simple words, Prognosis = What will probably happen next with the disease?")
    st.write("It can be:")
    st.write("- Good 👉 Likely to recover or live long")
    st.write("- Poor 👉 Disease may spread, come back, or reduce life expectancy")

  if ("predict" in t1) or ("prediction" in t1):
    data = pd.read_csv(d)
    data = data.dropna()
    data["10 year mortality"] = ((data["Overall Survival (Months)"] >= 120) & (data["Patient's Vital Status"] == "Living")).astype(int)
    data1 = data.copy()
    l = preprocessing.LabelEncoder()
    for i in data1.columns: # iterate through each columns, if datatype of the column is object datatype only then it will transform the data
       if data1[i].dtype == "object":
         data1[i] = l.fit_transform(data1[i])
    l = data1.drop(columns=["Patient ID","Sex"])
    data2 = l[(l["Patient's Vital Status"] != 0) & (l["Patient's Vital Status"] != 1)]
    data3 = data2.drop(columns=["Patient's Vital Status","Overall Survival Status"])
    x = data3.iloc[:,:-1]
    y = data3["10 year mortality"]
    x1 = data2.drop(columns=["Overall Survival (Months)","Patient's Vital Status","Overall Survival Status"])
    y1 = data2["Overall Survival (Months)"]

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier()
    rf.fit(x_train,y_train)
    y_pr = rf.predict(x_test)

    x1_train,x1_test,y1_train,y1_test = train_test_split(x1,y1,test_size=0.3,random_state=42)
    from sklearn.ensemble import RandomForestRegressor
    rf1 = RandomForestRegressor()
    rf1.fit(x1_train,y1_train) # Fit rf1 with x1_train an  st set x1_test
    y_pr2 = rf1.predict(x1_test)
    output = pd.DataFrame({"mortality":y_pr,"survival":y_pr2})
    #output = st.dataframe(output)
    cat = []
    for i in output.index:
      x = output.loc[i,"mortality"]
      y = output.loc[i,"survival"]
      if 60 <= y < 120:
        cat.append("5 year")
      elif 120 <= y < 180:
        cat.append("10 year")
      elif 180 <= y < 240:
        cat.append("15 year")
      elif 240 <= y < 300:
        cat.append("20 year")
      else:
        cat.append("< 5 year")
    output["survival in years"] = cat
    #output = st.dataframe(output)
    output["survival in years"].value_counts()
    cat_graph = pd.DataFrame({"survival in years":output["survival in years"].value_counts().index,"count":output["survival in years"].value_counts().values})
    st.write("Yeah, sure! Since you have the dataset, I will show the predictions, of sample size of 146 patients, regarding how many years they will survive. For this, advanced machine learning algorithm is used to predict as well as show insights of it.")
    st.subheader("Survival of patients year wise")
    f = px.bar(cat_graph,x="survival in years",y="count",color="survival in years")
    st.plotly_chart(f,use_container_width=True,height=200)
    st.write("So, from this insight, it is observed that, out of smaple size of 146 patients, 43 patients will survive from 15 to 20 years, 38 patients will survive from 10 to 15 years, 33 patients from 5 to 10 years, 23 patients will survive for more than 20 years, and rest 9 patients will survive less than 5 years. ")

    o1 = output[output["mortality"] == 1]
    s1 = float(o1["survival"].mean())
    v1 = o1["mortality"].value_counts()
    o2 = output[output["mortality"] == 0]
    s2 = float(o2["survival"].mean())
    v2 = o2["mortality"].value_counts()
    out1 = pd.DataFrame({"survival days":s1,"10 year survival count":v1.values,"status":[1]})
    out2 = pd.DataFrame({"survival days":s2,"10 year survival count":v2.values,"status":[0]})
    f1 = px.bar(pd.concat([out1,out2]),x="status",y="10 year survival count",color="status")
    st.subheader("Survival of patients above 10 years.")
    st.plotly_chart(f1,use_container_width=True,height=200)
    st.write("This is a simple insight that states that 104 patients will survive more than 10 years, and rest 42 patients will die before 10 years, out of 146 sample patient size.")
#st.sidebar.title("Add file")
