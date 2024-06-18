from flask import Flask
import toml
from flask_cors import CORS, cross_origin
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.instrumentation.flask import FlaskInstrumentor

from flask_openapi3 import Info
from flask_openapi3 import OpenAPI

info = Info(title="Flask Interoperability (A Microservice)", version="1.0.0")


def create_app(config_file):
    provider = TracerProvider(resource=Resource.create({SERVICE_NAME: "packt-flask-service"}))
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)

    # Sets the global default tracer provider
    trace.set_tracer_provider(provider)
    
    # Creates a tracer from the global tracer provider
    jaeger_exporter = JaegerExporter(agent_host_name="localhost", agent_port=6831,)
    trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(jaeger_exporter))
    
    global tracer
    tracer = trace.get_tracer("packt-flask-tracer")
    
    
    app = OpenAPI(__name__, info=info)
    app.config.from_file(config_file, toml.load)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    FlaskInstrumentor(app).instrument(enable_commenter=True, commenter_options={})
   

    with app.app_context():  
        from modules.api import users
        
    return app