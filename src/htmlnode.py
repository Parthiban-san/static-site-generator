class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_props = ''
        for i in self.props:
            html_props += f"""{i}="{self.props[i]}" """
        return html_props
    
    def __repr__(self):
        return f"""HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"""
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        has_tag = True if self.tag else False
        has_value = True if self.value else False
        has_children = True if self.children else False
        has_props = True if self.props else False

        if has_value == False:
            raise ValueError
        if has_tag == False:
            return self.value
        if has_props:
            rend_stmt = super().props_to_html()
            return f"""<{self.tag} {rend_stmt if rend_stmt else ''}>{self.value}</{self.tag}>"""
        
        return f"""<{self.tag}>{self.value}</{self.tag}>"""