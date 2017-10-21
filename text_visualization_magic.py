import shortuuid
import webbrowser
import os

sentree_format = """
                    <html>
                    <body>
                        <div id="vis"></div>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.9.1/d3.min.js"></script>
                        <script src="https://rawgit.com/twitter/SentenTree/master/dist/sententree-standalone.min.js"></script>
                        <script>
                            const path = "{file_path}"
                            d3.tsv(path, function(error, data) {{
                            data.forEach(d => {{
                                d.count = + d.count;
                            }})
                            const model = new SentenTree.SentenTreeBuilder().buildModel(data);
                            new SentenTree.SentenTreeVis('#vis').data(model.getRenderedGraphs(3))
                            .on('nodeClick', node => {{
                                console.log('node', node);
                                }});
                            }});
                        </script>
                    </body>
                    </html>
                    """



def text_visualization(line, text_path=''):
    temporary_output = '{}.html'.format(shortuuid.uuid())

    with open(temporary_output, 'w+') as f_output:
        f_output.write(sentree_format.format(file_path= text_path))
    
    webbrowser.get('firefox').open('file:///{}/{}'.format(os.getcwd(), temporary_output))
    os.remove(temporary_output)



def load_ipython_extension(ipython):
    ipython.register_magic_function(postgresql_syntax_checker, 'cell', 'text_visualization')



