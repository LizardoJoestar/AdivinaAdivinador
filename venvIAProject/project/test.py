import pytholog as pl

new_kb = pl.KnowledgeBase("flavor")
new_kb(["likes(noor, sausage)",
        "likes(melissa, pasta)",
        "likes(dmitry, cookie)",
        "likes(nikita, sausage)",
        "likes(assel, limonade)",
        "food_type(gouda, cheese)",
        "food_type(ritz, cracker)",
        "food_type(steak, meat)",
        "food_type(sausage, meat)",
        "food_type(limonade, juice)",
        "food_type(cookie, dessert)",
        "flavor(sweet, dessert)",
        "flavor(savory, meat)",
        "flavor(savory, cheese)",
        "flavor(sweet, juice)",
        "food_flavor(X, Y) :- food_type(X, Z), flavor(Y, Z)",
        "dish_to_like(X, Y) :- likes(X, L), food_type(L, T), flavor(F, T), food_flavor(Y, F), neq(L, Y)"])

print(new_kb.query(pl.Expr("likes(noor, sausage)")))
# ['Yes']

print(new_kb.query(pl.Expr("likes(noor, pasta)")))
# ['No']

print(new_kb.query(pl.Expr("dish_to_like(noor, What)")))

# Test lines
# tomasAquino = kb.query(pl.Expr("available_at_campus(X, tomasaquino)"))
# otay = kb.query(pl.Expr("available_at_campus(X, otay)"))

# print(tomasAquino)
# print(otay)