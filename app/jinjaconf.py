import jinja2
def messenger(d1, r1, d2):
    templateLoader = jinja2.FileSystemLoader( searchpath="/" )
    templateEnv = jinja2.Environment( loader=templateLoader )
    TEMPLATE_FILE = "~/Workspaces/ellingtonia/templates/example1.jinja"
    template = templateEnv.get_template( TEMPLATE_FILE )
    templateVars =  { 
                        "title" : "tab title",
                        # "depth" : d1,
                        "root": r1,
                        "dirs": d2,
                    }

    f = open('~/Workspaces/ellingtonia/outputs/output.html', 'a')
    f.write(template.render( templateVars ))
    