import pytholog as pl

kb = pl.KnowledgeBase("MrWho") 

kb([
    # Instead of prolog's "dif", use pytholog's "neq"
    # FACTS
    "dividedin(tec, unit)",
    "is_tec_campus(otay)",
    "is_tec_campus(tomasaquino)",

    "partof(systems, tomasaquino)",
    "partof(electromechanics, tomasaquino)",
    "partof(biochemistry, tomasaquino)",
    "partof(industrial, tomasaquino)",

    "partof(architecture, otay)",
    "partof(biomedics, otay)",
    "partof(tics, otay)",
    "partof(mechanics, otay)",
    "partof(accounting, otay)",
    "partof(civil, otay)",

    # Computer Sytems
    "uses(systems, linux)",
    "uses(systems, software)",
    "uses(systems, sdlc)",

    # TICS
    "uses(tics, mass_media)",
    "uses(tics, linux)",

    # Mechanical Engineering
    "uses(mechanics, materialscience)",
    "uses(mechanics, cad)",

    # Architecture
    "uses(architecture, model)",
    "uses(architecture, trule)",
    "uses(architecture, artisticdrawings)",

    # Biomedics
    "uses(biomedics, medicine)",
    "uses(biomedics, labcoats)",
    "uses(biomedics, test_tubes)",

    # Biochemistry
    "uses(biochemistry, organic_chemistry)",
    "uses(biochemistry, test_tubes)",
    "uses(biochemistry, labcoats)",

    # Industrial Engineering
    "uses(industrial, quality_control)",
    "uses(industrial, mass_production)",
    "uses(industrial, trule)",
    "uses(industrial, cad)",

    # Civil Engineering
    "uses(civil, topography)",
    "uses(civil, blueprints)",
    "uses(civil, trule)",

    # Electromechanics
    "uses(electromechanics, electricity)",
    "uses(electromechanics, oscilloscope)",
    "uses(electromechanics, cad)",

    # Accounting
    "uses(accounting, active_pasives)",
    "uses(accounting, balancing)",

    # RULES
    "usedbysystems(X):- uses(systems, X)",
    "usedbymechanics(X):- uses(mechanics, X)",
    "usedbyarchitecture(X):- uses(architecture, X)",
    "usedbybiomedics(X):- uses(biomedics, X)",
    "same_campus(X, Y):- neq(X, Y), partof(X, Z), partof(Y, Z), is_tec_campus(Z)","used_by_same_major(X, Y):- neq(X, Y), uses(Z, X), uses(Z, Y)","available_at_campus(X, Y):- is_tec_campus(Y), partof(X, Y)",
    "used_by_major(X, Y, Z):- used_by_same_major(Y, Z), uses(X, Y), uses(X, Z), partof(X, W), is_tec_campus(W)",
    "use_same_tools(X, Y):- neq(X, Y), partof(X, M), partof(Y, N), is_tec_campus(M), is_tec_campus(N), uses(X, W), uses(Y, W)"
])
