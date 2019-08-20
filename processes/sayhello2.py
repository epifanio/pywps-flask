
from pywps import Process, LiteralInput, LiteralOutput, UOM



class SayHello2(Process):
    def __init__(self):
        inputs = [LiteralInput('name', 'Input name', data_type='string')]
        outputs = [LiteralOutput('response',
                                 'Output response', data_type='string')]

        super(SayHello2, self).__init__(
            self._handler,
            identifier='say_hello2',
            title='Process Say Hello2',
            abstract='Returns a literal string output\
             with Hello plus the inputed name',
            version='1.3.3.7',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        response.outputs['response'].data = 'Hello ' + \
            request.inputs['name'][0].data
        response.outputs['response'].uom = UOM('unity')
        return response
