class TrigBiPyMVP:
    def __init__(self, axioms):
        self.S = set()  # Sources (Rohdaten / Zeugenaussagen)
        self.O = set()  # Observations (extrahierte harte Fakten)
        self.T = set()  # Theories (stabile Erklärungsmodelle)
        self.D = set()  # Discourses (Widersprüche / Anomalien)
        self.Axioms = axioms  # Invariante epistemische Constraints
        
    def add_source(self, s):
        print(f"[Operation S] Neue Quelle injiziert: '{s['text']}'")
        self.S.add(s["text"])
        
    def observe(self, s, extract_func):
        # S x T -> O (theoriegeladene Wahrnehmung)
        o = extract_func(s)
        print(f"[Operation S x T -> O] Beobachtung extrahiert: {o}")
        o_frozen = tuple(sorted(o.items()))
        self.O.add(o_frozen)
        return o
        
    def collide(self, o1, o2):
        print(f"\n[Operation O x O] Kollidiere Beobachtungen:\n  1: {o1}\n  2: {o2}")
        # Prüfung auf Synthese (T) oder Anomalie (D)
        for axiom in self.Axioms:
            if not axiom.validate(o1, o2):
                # Pullback Obstruction -> Diskurs
                d = f"Konflikt: {o1['person']} in {o1['location']} vs. {o2['location']} ({axiom.name})"
                self.D.add(d)
                print(f"  -> ERGEBNIS: D (Diskurs) | {d}")
                return d
                
        # Kommutativität hergestellt -> Synthese
        t = f"Synthese: {o1['person']} & {o2['person']} kompatibel ({o1['location']} / {o2['location']})"
        self.T.add(t)
        print(f"  -> ERGEBNIS: T (Theorie) | {t}")
        return t

    def print_state(self):
        print("\n" + "="*50)
        print("AKTUELLE EPISTEMISCHE MENGEN (TrigBiPy State)")
        print("="*50)
        print(f"|S| Quellen       : {list(self.S) if self.S else '[]'}")
        print(f"|O| Beobachtungen : {list(self.O) if self.O else '[]'}")
        print(f"|T| Theorien      : {list(self.T) if self.T else '[]'}")
        print(f"|D| Diskurse      : {list(self.D) if self.D else '[]'}")
        print("="*50 + "\n")


class Axiom:
    def __init__(self, name, rule):
        self.name = name
        self.validate = rule

# Axiom: Gesetz der Bilokation (niemand kann an zwei Orten gleichzeitig sein)
bilocation_impossible = Axiom(
    "Gesetz der Bilokation", 
    lambda x, y: not (x['person'] == y['person'] and x['time'] == y['time'] and x['location'] != y['location'])
)

system = TrigBiPyMVP([bilocation_impossible])

print("\n--- TrigBiPy Epistemischer Linter (Kriminalfall-Edition) ---\n")
# Dieses MVP demonstriert die Funktionsweise von TrigBiPy als deterministischer Zustandsmaschine.
# Es wird gezeigt, wie durch die Injektion von Rohdaten (Quellen) theoriegeladene Beobachtungen
# generiert werden und diese in einer algebraischen Kollision entweder in einem stabilen 
# theoriebildenden Zustand (T) oder einem unlösbaren Diskurs (D) enden.

# 1. Injektion von Quellen
# Gemäß dem "Gesetz der blinden Daten" (S x S -> Ø) haben diese Quellen für das System 
# noch keine inhärente Bedeutung und können nicht direkt interagieren.
s1 = {"text": "Zeuge 1 sagt: Ich habe Alice um 20:00 Uhr in der Küche gesehen."}
s2 = {"text": "Zeuge 2 sagt: Ich schwöre, Alice war um 20:00 Uhr draußen im Garten."}
s3 = {"text": "Kameraaufzeichnung: Bob war um 20:00 Uhr im Flur zu sehen."}

system.add_source(s1)
system.add_source(s2)
system.add_source(s3)

# 2. Theoriegeladene Wahrnehmung
print("\n--- Extraktion der Fakten ---")
# Operation S x T -> O: Quellen (S) werden durch ein Modell interpretiert,
# da eine interpretationsfreie Wahrnehmung in TrigBiPy nicht existiert.
o1 = system.observe(s1, lambda s: {'person': 'Alice', 'location': 'Küche', 'time': '20:00'})
o2 = system.observe(s2, lambda s: {'person': 'Alice', 'location': 'Garten', 'time': '20:00'})
o3 = system.observe(s3, lambda s: {'person': 'Bob', 'location': 'Flur', 'time': '20:00'})

# 3. Algebraische Kollision (Bifurkation in T oder D)
print("\n--- System prüft Kommutativität ---")
# Hier greifen die "Epistemischen Naturgesetze": Wir prüfen ob ein Pullback-Objekt (T) 
# gebildet werden kann, ohne dass die Axiomatik ($A \subseteq T$) verletzt wird.
system.collide(o1, o2)  # Konflikt (Alice an 2 Orten) -> Pullback Obstruction -> Diskurs (D)
system.collide(o1, o3)  # Synthese (Alice & Bob an versch. Orten) -> Stabilisierung in Theorie (T)

# 4. Finaler Systemzustand
# Das System zeigt am Ende die asymptotischen Attraktoren (Theorien) und die 
# ungelösten Inkohärenzen (Diskurse), welche die "epistemische Entropie" bilden.
system.print_state()
