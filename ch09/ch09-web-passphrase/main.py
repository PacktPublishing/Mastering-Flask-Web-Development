from modules import create_app


app = create_app('../config_dev.toml')

@app.after_request
def create_sec_resp_headers(response):
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['Strict-Transport-Security'] = 'Strict-Transport-Security: max-age=63072000; includeSubDomains; preload'
    return response

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))
    