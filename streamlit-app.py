import streamlit as st
import pandas as pd

import io
from io import StringIO

import classifier as cl 
import regressor as reg 

# Import necessary modules
import pandas as pd
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn import preprocessing 
from lazypredict.Supervised import LazyClassifier
from lazypredict.Supervised import LazyRegressor

import matplotlib.pyplot as plt

label   = preprocessing.LabelEncoder() 


def main():
    st.title("Instinctive Data Analysis")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # # To read file as bytes:
        # bytes_data = uploaded_file.getvalue()
        # st.write(bytes_data)

        # # To convert to a string based IO:
        # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # st.write(stringio)

        # # To read file as string:
        # string_data = stringio.read()
        # st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        
        col1, col2, col3 = st.columns([1,1,1])

        # st.write(uploaded_file)
        # for var in uploaded_file:
        #     st.write(uploaded_file.index(var),var)
    
        # with col1:
        #     st.button('1')
        with col2:
            if st.button('Classifier'):
                # result = cl.classifier(uploaded_file)
                # final = pd.DataFrame.from_dict(result)
                # st.write(result)
                # st.table(final)

                # df      =  pd.read_csv(uploaded_file)
                missing = df.isnull().values.any()

                if missing == True:
                    df = df.ffill().bfill()
                    print("null values filled")
                else:
                    print("no null values encountered")
                
                object_col = df.select_dtypes(include=['object']).columns

                for name in object_col:
                    df[name] = label.fit_transform(df[name]) 

                df.drop_duplicates(inplace=True)

                X = df.iloc[:,:-1]
                Y = df[df.columns[-1]]

                X_train, X_test, Y_train, Y_test =train_test_split(X,Y,test_size=.3,random_state =23)
                classi=LazyClassifier(verbose=0,predictions=True)

                models_c, predictions_c = classi.fit(X_train, X_test, Y_train, Y_test)

                st.write(models_c)

                plot_df = pd.DataFrame(models_c)

                plot_df = plot_df.reset_index()

                print(plot_df)

                plt.rcParams["figure.figsize"] =[16,9]
                plot_df.plot(x="Model",y="Accuracy",color="Red",kind="line",marker='o',markersize=12)
                plt.xlabel("Model")
                plt.ylabel('Accuracy')
                plt.grid()
                plt.show()

                # fig, ax = plt.subplots()
                # ax.scatter([1, 2, 3], [1, 2, 3])
                
                # st.pyplot(fig)
                st.set_option('deprecation.showPyplotGlobalUse', False)

                st.pyplot(x="Model",y="Accuracy")

                return models_c

            
        with col3:
            if st.button('Regressor'):
                # df = pd.read_csv(CSV_FILE_PATH)
                missing = df.isnull().values.any()

                if missing == True:
                    df = df.ffill().bfill()
                    print("null values filled")
                else:
                    print("no null values encountered")
                
                object_col = df.select_dtypes(include=['object']).columns

                for name in object_col:
                    df[name] = label.fit_transform(df[name]) 

                df.drop_duplicates(inplace=True)

                X = df.iloc[:,:-1]
                y = df[df.columns[-1]]

                X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=.3,random_state =123)
                reg = LazyRegressor(verbose=0,ignore_warnings=True, custom_metric=None)

                models,predictions = reg.fit(X_train, X_test, y_train, y_test)
                
                st.write(models)

                plot_data = pd.DataFrame(models)
                plot_data = plot_data.reset_index()

                plt.rcParams["figure.figsize"] =[16,9]
                plot_data.plot(x="Model",y="RMSE",color="Red",kind="line",marker='o',markersize=12)
                plt.xlabel("Model")
                plt.ylabel('RMSE')
                plt.grid()
                plt.show()

                st.set_option('deprecation.showPyplotGlobalUse', False)

                st.pyplot(x="Model",y="RMSE")

                return models



if __name__ == "__main__":
    main()