from fasthtml.common import *

# HTMx - HTML
# picocss - CSS

app,rt = fast_app()

counter = 0
@rt('/')
def get(): 
    return Div(
        Table(
            Thead(
                Th('First Name', 'Last Name'),
            ),
            Tbody(
                Tr(
                    Td('John'), Td('Doe')
                )
            ),
        ),
        P('Hello World'),
        Button('Add', hx_get="/add"),
        Button('Substract', hx_get="/substract")
    )

@rt('/change')
def get(): 
    return P('Nice to be here!')

@rt('/add')
def get(): 
    global counter
    counter += 1
    return Span(f'Counter: {counter}')

@rt('/substract')
def get(): 
    global counter
    counter -= 1
    return counter

@rt('/contact')
def get(): 
    return Div(
        H1('Contact Form'),
        Form(
            
            Input(type='text', name='name', placeholder='Name'),
            Input(type='email', name='email', placeholder='Email'),
            Input(type='text', name='message', placeholder='Message'),
            Button(type='submit', value='Submit', label="Submit"),
        )
    )


serve()