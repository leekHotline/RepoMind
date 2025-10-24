import gradio as gr

# 要把全局代理关闭


def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"


demo = gr.Interface(
    fn=calculator,
    inputs=[
        gr.Number(label="Number 1"),
        gr.Dropdown(label="Operation", choices=[
                    "add", "subtract", "multiply", "divide"]),
        gr.Number(label="Number 2"),
    ],
    outputs=gr.Number(label="Result"),
    title="simple calculator",
    description="Enter two numbers and select an operation to perform"
)

demo.launch()
