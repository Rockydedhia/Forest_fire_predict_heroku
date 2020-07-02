import streamlit as st
import pickle
import numpy as np

model = pickle.load ( open ( "model.pkl", "rb" ) )


def predict_forest(oxygen, humidity, tempearture) :
    input = np.array ( [[oxygen, humidity, tempearture]] ).astype ( np.float64 )
    predict = model.predict_proba ( input )
    pred = "{0:.{1}f}".format ( predict[0][1], 2 )
    print ( pred )
    return float ( pred )


def main() :
    st.title ( "First Deployment Tutuorial" )
    html = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;test-align:center;">Forest Fire Predicition</h2>
    </div>
    """
    st.markdown ( html, unsafe_allow_html=True )
    oxygen = st.slider ( "Select Oxygen Level",0,100 )
    humidity = st.slider ( "Select Humidity Level",0,100 )
    tempearture = st.slider ( "Selct Tepearture Level",0,100 )
    safe = """
     <div style="background-color:#4D03F ;padding:10px">
    <h2 style="color:white;test-align:center;">YOUR FOREST IS SAFE! </h2>
    </div>
    """
    danger = """
     <div style="background-color:#F08080 ;padding:10px">
    <h2 style="color:white;test-align:center;">YOUR FOREST IS IN DNAGER</h2>

    </div>
    """

    if st.button ( "Predicit" ) :
        output = predict_forest ( oxygen, humidity, tempearture )
        st.success ( "The Probability of Fire Taking place is {}".format ( output ) )

        if output > 0.5 :
            st.markdown ( danger, unsafe_allow_html=True )
        else :
            st.markdown ( safe, unsafe_allow_html=True )

if __name__ == "__main__" :
    main ()
