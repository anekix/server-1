import falcon

class ThingsResource:
    def on_get(self, req, resp,form={},files={}):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ("GET request accepted")
        
    def on_post(self, req, resp,form={},files={}):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        #resp.content_type = 'application/text'
        #print(form["id"]) -> value captured from hook defined in common.py 
        resp.body = ("POST request accepted")
 

