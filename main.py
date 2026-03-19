import numpy as np
import joblib
model=joblib.load('random_forest_model.pkl')
from flask import Flask , render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/features')
def features():
    return render_template('features.html')
@app.route('/how-to-work')
def how_to_work():
    return render_template('howtowork.html')
@app.route('/predict',methods=['POST','GET'])
def predict():
      if request.method=='POST':  
                
                brand=request.form.get('brand')
                processor_brand=request.form.get('processor_brand')
                processor_name=request.form.get('processor_name')
                processor_gnrtn=request.form.get('processor_gnrtn')
                ram_gb=request.form.get('ram_gb')
                ram_type=request.form.get('ram_type')
                ssd=request.form.get('ssd')
                hdd=request.form.get('hdd')
                os=request.form.get('os') 
                os_bit=int(request.form.get('os_bit')) 
                graphic_card_gb=request.form.get('graphic_card_gb')   
                weight=request.form.get('weight') 
                
                warranty=request.form.get('warranty') 
                Touchscreen=request.form.get('Touchscreen') 
                msoffice=request.form.get('msoffice') 
                # print("kii mera jo data hai vo upload ho gya")
                print(">>>>>>",brand)
                brand_dict={
                'ASUS':10, 'Lenovo':20, 'acer':30, 'Avita':40, 'HP':50, 'DELL':60, 'MSI':70, 'APPLE':80
                    }
                brand=brand_dict[brand]


                processor_brand_dict={
                'Intel':1, 'AMD':2, 'M1':3
                    }
                processor_brand=processor_brand_dict[processor_brand]

                processor_name_dict={
                    'Core i3':3,      'Core i5':5, 'Celeron Dual':1,      'Ryzen 5':6,
                    'Core i7':7,      'Core i9':9,           'M1':4, 'Pentium Quad':2,
                    'Ryzen 3':11,      'Ryzen 7':8,      'Ryzen 9':10
                }
                processor_name=processor_name_dict[processor_name]

                processor_gnrtn_dict={
    '10th':10, 'Not Available':0, '11th':11, '7th':7, '8th':8, '9th':9, '4th':4, '12th':12
                }
                processor_gnrtn=processor_gnrtn_dict[processor_gnrtn]

                ram_gb_dict={
    '4 GB':4, '8 GB':8, '16 GB':16, '32 GB':32
                }
                ram_gb=ram_gb_dict[ram_gb]

                ram_type_dict={
    'DDR4':1, 'LPDDR4':2, 'LPDDR4X':3, 'DDR5':4, 'DDR3':5, 'LPDDR3':6
                }
                ram_type=ram_type_dict[ram_type]

                ssd_dict={
    '0 GB':0, '512 GB':512, '256 GB':256, '128 GB':128, '1024 GB':1024, '2048 GB':2048, '3072 GB':3072
}
                ssd=ssd_dict[ssd]

                hdd_dict={
    '1024 GB':1024, '0 GB':0, '512 GB':512, '2048 GB':2048
}
                hdd=hdd_dict[hdd]

                os_dict={
    'Windows':1, 'DOS':2, 'Mac':3
    }
                os=os_dict[os]

                graphic_card_gb_dict={
    '0 GB':0, '2 GB':2, '4 GB':4, '6 GB':6, '8 GB':8
}
                graphic_card_gb=graphic_card_gb_dict[graphic_card_gb]

                weight_dict={
    'Casual':1, 'ThinNlight':2, 'Gaming':3
}
                weight=weight_dict[weight]

                warranty_dict={
    'No warranty':0, '1 year':1, '2 years':2, '3 years':3
}
                warranty=warranty_dict[warranty]

                Touchscreen_dict={
    'No':0, 'Yes':1
}
                Touchscreen=Touchscreen_dict[Touchscreen]

                msoffice_dict={
    'No':0, 'Yes':1
}
                msoffice=msoffice_dict[msoffice]

                print("lables:-",brand,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb,weight,warranty,Touchscreen,msoffice)
                lables=[[brand,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb,weight,warranty,Touchscreen,msoffice]]
                pred=model.predict(lables)
                print(type(pred))
                pred=np.ravel(pred)
                print("output:-",pred)
                return render_template('predict.html',prediction=pred[0])
      
      return render_template('predict.html')



if __name__=="__main__":
        app.run(debug=True)


