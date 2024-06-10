def create_index_routes(app):

    @app.route('/home')
    @app.route('/information')
    @app.route('/introduction')
    def home():
        return '''
                <html>
                    <head>
                        <title>Online Personal Counseling System</title>
                    </head>
                    <body>
                        <h1>Online Personal Counseling System (OPCS)</h1>
                        <p>This is a template of a web-based counseling application where
                        counselors can interact with their patients through evaluations
                        and examinations. This application is managed by a group of
                        administrators to monitor the interactions between profiles.
                        <em>Sherwin John Tragura, developer</em>
                    </body>
                </html>
            '''


