import gradio as gr
import ollama

def process_input(image, text):
    if image is None or not text:
        return "Please provide both an image and a text prompt."
    
    try:
        response = ollama.chat(
            model='llama3.2-vision:11b',
            messages=[{
                'role': 'user',
                'content': text,
                'images': [image]  # Image is passed directly from Gradio
            }]
        )
        return response.get("message", {}).get("content", "No response from the model.")
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio Interface
iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.Image(type="filepath"),  # Removed 'source="upload"'
        gr.Textbox(label="Enter your question"),
    ],
    outputs="text",
    title="Ollama Vision Chat",
    description="Upload an image and ask a question about it.",
)

# Launch Gradio app on local network
iface.launch(server_name="192.168.0.105", server_port=7860)
