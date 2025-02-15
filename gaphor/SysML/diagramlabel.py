from gaphor.diagram.diagramlabel import diagram_label
from gaphor.SysML.sysml import SysMLDiagram, Block, ConstraintBlock, Requirement
from gaphor.UML.uml import Activity, Package, Interaction, Profile, StateMachine


@diagram_label.register(SysMLDiagram)
def sysml_diagram_label(diagram):
    def element_type(el):
        if isinstance(el, Activity):
            return "activity"
        if isinstance(el, ConstraintBlock):
            return "constraint block"
        if isinstance(el, Block):
            return "block"
        if isinstance(el, Interaction):
            return "interaction"
        if isinstance(el, Profile):
            return "profile"
        if isinstance(el, Package):
            return "package"
        if isinstance(el, Requirement):
            return "requirement"
        if isinstance(el, StateMachine):
            return "state machine"
        return ""

    if diagram.element:
        return (
            f"[{element_type(diagram.element)}] {diagram.element.name} [{diagram.name}]"
        )
    else:
        # TODO: SysML specification does not allow parentless elements, but since it is not constrained (yet), it may happen.
        return diagram.name
