# http://protege.stanford.edu/protege/3.4/docs/api/owl/edu/stanford/smi/protegex/owl/model/OWLModel.html

def create_owl_class(className):
    created_class = kb.createOWLNamedClass(className)
    
    return created_class
    
def create_owl_subclass(subclass_name, classobject):
    created_subclass = kb.createOWLNamedSubclass(subclass_name, classobject)
    
    return created_subclass
    
class_names = ['charactersticname', 'measureunitcode', 'parameter_cd']

for class_name in class_names:
    create_owl_class(class_name)