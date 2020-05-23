if __name__ is not None and "." in __name__:
    from cl.SkylineParser import SkylineParser
    from cl.SkylineVisitor import SkylineVisitor
else:
    from cl.SkylineParser import SkylineParser
    from cl.SkylineVisitor import SkylineVisitor

from Skyline import Skyline, WrongArgumentException


class EvalVisitor(SkylineVisitor):
    def __init__(self, skylines):
        self.skylines = skylines

    def visitRoot(self, ctx):
        n = next(ctx.getChildren())
        return self.visit(n)

    def visitBase_expr(self, ctx):
        # Case 1: The base_expr is an expr
        if ctx.getChildCount() == 1:
            return self.visit(next(ctx.getChildren()))

        # Case 2: The base_expr is identifier ASSIG expr
        else:
            identifier = self.visit(ctx.identifier())
            sky = self.visit(ctx.expr())
            self.skylines[identifier] = sky
            return sky

    def visitExpr(self, ctx):
        is_paren = ctx.LEFT_PAREN() or ctx.RIGHT_PAREN()

        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            result = self.visit(n)
            # Case 1: The expr is an identifier
            if isinstance(result, str):
                try:
                    return self.skylines[result]
                except:
                    raise WrongArgumentException(f"{result} no és un identificador definit")
            # Case 2: The expr is a constructor
            else:
                return result

        # Case 3: The expr is a parentheses
        elif is_paren:
            return self.visit(ctx.expr(0))

        # Case 4: The expr is a unary minus
        elif ctx.MINUS() and ctx.getChildCount() == 2:  # TOCHECK
            return self.visit(ctx.expr(0)).invert()

        # Case 5: The expr is anything else
        else:
            # Ignore the middle child, which is the operator
            op1, op2 = list(ctx.getChildren())[::2]
            if ctx.PLUS():
                return Skyline.add(self.visit(op1), self.visit(op2))

            elif ctx.PROD():
                return Skyline.prod(self.visit(op1), self.visit(op2))

            else:
                return Skyline.subtract(self.visit(op1), self.visit(op2))

    def visitConstructor(self, ctx):
        return self.visit(next(ctx.getChildren()))

    def visitSingle_building(self, ctx):
        params = []
        for child in ctx.getChildren():
            param = self.visit(child)
            if param is not None:
                params.append(param)
        return Skyline.create_from_building(*params)

    def visitMultiple_buildings(self, ctx):
        params = []
        for child in ctx.getChildren():
            param = self.visit(child)
            if param is not None:
                params.append(param)
        return Skyline.create_from_buildings(params)

    def visitRandom_buildings(self, ctx):
        params = []
        for child in ctx.getChildren():
            param = self.visit(child)
            if param is not None:
                params.append(param)
        return Skyline.create_from_random_buildings(*params)

    def visitNum(self, ctx):
        n = next(ctx.getChildren())
        return int(n.getText())

    def visitIdentifier(self, ctx):
        n = next(ctx.getChildren())
        return n.getText()
