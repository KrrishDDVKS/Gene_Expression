import streamlit as st
import pandas as pd
import numpy as np
import joblib
def main():
    st.title("Cancer Personalized Treatment through Gene Expression")
    st.write("This application aims to provide personalized treatment recommendations for cancer patients based on their gene expression profiles.")
    st.write("Users can input their gene expression data, and the application will analyze it to suggest potential treatment options tailored to the individual's genetic profile.")
    st.write("Please input the gene expression values for the patient:")

    gene_expression_1=st.slider("Enter gene expression value1", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_1")
    gene_expression_2=st.slider("Enter gene expression value2", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_2")
    gene_expression_3=st.slider("Enter gene expression value3", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_3")
    gene_expression_4=st.slider("Enter gene expression value4", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_4")
    gene_expression_5=st.slider("Enter gene expression value5", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_5")
    gene_expression_6=st.slider("Enter gene expression value6", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_6")
    gene_expression_7=st.slider("Enter gene expression value7", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_7")
    gene_expression_8=st.slider("Enter gene expression value8", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_8")
    gene_expression_9=st.slider("Enter gene expression value9", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_9")
    gene_expression_10=st.slider("Enter gene expression value10", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_10")
    gene_expression_11=st.slider("Enter gene expression value11", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_11")
    gene_expression_12=st.slider("Enter gene expression value12", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_12")
    gene_expression_13=st.slider("Enter gene expression value13", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_13")
    gene_expression_14=st.slider("Enter gene expression value14", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_14")
    gene_expression_15=st.slider("Enter gene expression value15", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_15")
    gene_expression_16=st.slider("Enter gene expression value16", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_16")
    gene_expression_17=st.slider("Enter gene expression value17", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_17")
    gene_expression_18=st.slider("Enter gene expression value18", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_18")
    gene_expression_19=st.slider("Enter gene expression value19", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_19")
    gene_expression_20=st.slider("Enter gene expression value20", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_20")
    gene_expression_21=st.slider("Enter gene expression value21", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_21")
    gene_expression_22=st.slider("Enter gene expression value22", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_22")
    gene_expression_23=st.slider("Enter gene expression value23", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_23")
    gene_expression_24=st.slider("Enter gene expression value24", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_24")
    gene_expression_25=st.slider("Enter gene expression value25", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_25")
    gene_expression_26=st.slider("Enter gene expression value26", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_26")
    gene_expression_27=st.slider("Enter gene expression value27", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_27")
    gene_expression_28=st.slider("Enter gene expression value28", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_28")
    gene_expression_29=st.slider("Enter gene expression value29", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_29")
    gene_expression_30=st.slider("Enter gene expression value30", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_30")
    gene_expression_31=st.slider("Enter gene expression value31", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_31")
    gene_expression_32=st.slider("Enter gene expression value32", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_32")
    gene_expression_33=st.slider("Enter gene expression value33", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_33")
    gene_expression_34=st.slider("Enter gene expression value34", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_34")
    gene_expression_35=st.slider("Enter gene expression value35", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_35")
    gene_expression_36=st.slider("Enter gene expression value36", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_36")
    gene_expression_37=st.slider("Enter gene expression value37", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_37")
    gene_expression_38=st.slider("Enter gene expression value38", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_38")
    gene_expression_39=st.slider("Enter gene expression value39", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_39")
    gene_expression_40=st.slider("Enter gene expression value40", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_40")
    gene_expression_41=st.slider("Enter gene expression value41", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_41")
    gene_expression_42=st.slider("Enter gene expression value42", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_42")
    gene_expression_43=st.slider("Enter gene expression value43", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_43")
    gene_expression_44=st.slider("Enter gene expression value44", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_44")
    gene_expression_45=st.slider("Enter gene expression value45", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_45")
    gene_expression_46=st.slider("Enter gene expression value46", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_46")
    gene_expression_47=st.slider("Enter gene expression value47", min_value=0.0, max_value=1.0, value=0.0, key="gene_expression_47")
        
    joblib_model = joblib.load("survival.joblib")
    if st.button("Predict"):
        input_data = pd.DataFrame([[
            gene_expression_1, gene_expression_2, gene_expression_3, gene_expression_4, gene_expression_5,
            gene_expression_6, gene_expression_7, gene_expression_8, gene_expression_9, gene_expression_10,
            gene_expression_11, gene_expression_12, gene_expression_13, gene_expression_14, gene_expression_15,
            gene_expression_16, gene_expression_17, gene_expression_18, gene_expression_19, gene_expression_20,
            gene_expression_21, gene_expression_22, gene_expression_23, gene_expression_24, gene_expression_25,
            gene_expression_26, gene_expression_27, gene_expression_28, gene_expression_29, gene_expression_30,
            gene_expression_31, gene_expression_32, gene_expression_33, gene_expression_34, gene_expression_35,
            gene_expression_36, gene_expression_37, gene_expression_38, gene_expression_39, gene_expression_40,
            gene_expression_41, gene_expression_42, gene_expression_43, gene_expression_44, gene_expression_45,
            gene_expression_46, gene_expression_47
        ]])
        st.write("Input data:")
        st.write(input_data.shape)
        
        prediction = joblib_model.predict_survival_function(input_data)
        predicted_time = []
        for sf in prediction:
            if np.any(sf.y <= 0.5):
                t = sf.x[np.where(sf.y <= 0.5)[0][0]]
            else:
                t = sf.x[-1]
            predicted_time.append(t)
        risk = joblib_model.predict(input_data)
        threshold = 23.286096350408855
        print("Predicted Risk:", threshold)
        predicted_group = (risk > threshold).astype(int)

        results=pd.DataFrame()

        results["Predicted_Risk"] = risk
        results["Predicted_Time"] = predicted_time
        results["Risk_Group"] = predicted_group

        st.write(results)

        st.write("Predicted Risk:", risk[0])
        st.write("Predicted Time:", predicted_time[0])
        st.write("Risk Group:", predicted_group[0])
        if predicted_group[0] == 1:
            st.error("The patient is predicted to be in the high-risk group.")
        else:
            st.success("The patient is predicted to be in the low-risk group.")

if __name__ == "__main__":
    main()
