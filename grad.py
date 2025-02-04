import pickle
import gradio as gr

def predicted(total_bill,size,time):
    with open('tip.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    
    input_data = [[total_bill, size, time]]
    prediction = loaded_model.predict(input_data)[0]
    
    return str(prediction)

iface=gr.Interface(
    fn=predicted,
    inputs=[gr.Number(label='total_bill'),
            gr.Number(label='size'),
            gr.Number(label="time")
            ],
    outputs="text"
)

iface.launch(share=True)