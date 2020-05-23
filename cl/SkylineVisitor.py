# Generated from Skyline.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#base_expr.
    def visitBase_expr(self, ctx:SkylineParser.Base_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#constructor.
    def visitConstructor(self, ctx:SkylineParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#single_building.
    def visitSingle_building(self, ctx:SkylineParser.Single_buildingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#multiple_buildings.
    def visitMultiple_buildings(self, ctx:SkylineParser.Multiple_buildingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#random_buildings.
    def visitRandom_buildings(self, ctx:SkylineParser.Random_buildingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#identifier.
    def visitIdentifier(self, ctx:SkylineParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#num.
    def visitNum(self, ctx:SkylineParser.NumContext):
        return self.visitChildren(ctx)



del SkylineParser