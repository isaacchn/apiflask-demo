from mongoengine import Document, EmbeddedDocument, StringField, ListField, EmbeddedDocumentField


class StructureAttribute(EmbeddedDocument):
    """
    结构属性，K-V结构
    """
    attr_name = StringField(required=True, max_length=31)
    attr_description = StringField(required=True, max_length=255)


class Structure(Document):
    """
    结构
    """
    name = StringField(required=True, max_length=31, unique=True)
    description = StringField(required=True, max_length=255)
    parent_structure = StringField(required=False)
    attributes = ListField(EmbeddedDocumentField(StructureAttribute))
    # fields = ListField(StringField())


class InstanceAttribute(EmbeddedDocument):
    attr_name = StringField(required=True, max_length=31)
    attr_description = StringField(required=True, max_length=255)
    attr_value = StringField(required=True, max_length=255)
