# grammar_rules.py

# Lista ampliada de verbos en pasado
past_verbs = [
    "was", "were", "went", "saw", "played", "watched", "studied", "ran", "walked", "ate", "drank", "slept",
    "came", "bought", "brought", "built", "caught", "chose", "did", "dug", "drew", "dreamt", "drove", "fell", 
    "felt", "found", "flew", "forgot", "forgave", "froze", "got", "gave", "grew", "hung", "heard", "hid", "hit", 
    "held", "hurt", "kept", "knew", "laid", "led", "left", "lent", "let", "lost", "made", "meant", "met", "paid", 
    "put", "read", "rode", "rang", "rose", "ran", "said", "saw", "sold", "sent", "set", "shook", "shone", "shot", 
    "sang", "sat", "slept", "spoke", "spent", "stood", "stole", "swam", "took", "taught", "told", "thought", 
    "threw", "understood", "woke", "wore", "won", "wrote", "visited", "worked", "talked", "used", "called", 
    "tried", "asked", "needed", "felt", "became", "left", "put", "meant", "kept", "let", "began"
]

# Lista ampliada de verbos en presente simple
present_verbs = [
    "am", "are", "is", "go", "see", "play", "watch", "study", "run", "walk", "eat", "drink", "sleep", "come", 
    "buy", "bring", "build", "catch", "choose", "do", "dig", "draw", "dream", "drive", "fall", "feel", "find", 
    "fly", "forget", "forgive", "freeze", "get", "give", "grow", "hang", "hear", "hide", "hit", "hold", "hurt", 
    "keep", "know", "lay", "lead", "leave", "lend", "let", "lose", "make", "mean", "meet", "pay", "put", "read", 
    "ride", "ring", "rise", "run", "say", "see", "sell", "send", "set", "shake", "shine", "shoot", "sing", "sit", 
    "sleep", "speak", "spend", "stand", "steal", "swim", "take", "teach", "tell", "think", "throw", "understand", 
    "wake", "wear", "win", "write", "visit", "work", "talk", "use", "call", "try", "ask", "need", "feel", "become", 
    "leave", "put", "mean", "keep", "let", "begin"
]

# Lista de verbos en gerundio o participio presente
gerunds = [
    "being", "going", "seeing", "playing", "watching", "studying", "running", "walking", "eating", "drinking", 
    "sleeping", "coming", "buying", "bringing", "building", "catching", "choosing", "doing", "digging", "drawing", 
    "dreaming", "driving", "falling", "feeling", "finding", "flying", "forgetting", "forgiving", "freezing", 
    "getting", "giving", "growing", "hanging", "hearing", "hiding", "hitting", "holding", "hurting", "keeping", 
    "knowing", "laying", "leading", "leaving", "lending", "letting", "losing", "making", "meaning", "meeting", 
    "paying", "putting", "reading", "riding", "ringing", "rising", "running", "saying", "seeing", "selling", 
    "sending", "setting", "shaking", "shining", "shooting", "singing", "sitting", "sleeping", "speaking", 
    "spending", "standing", "stealing", "swimming", "taking", "teaching", "telling", "thinking", "throwing", 
    "understanding", "waking", "wearing", "winning", "writing", "working", "talking", "using", "calling", "trying"
]

past_participle_verbs = [
    "gone", "seen", "played", "watched", "studied", "run", "walked", "eaten", "drunk", "slept",
    "come", "bought", "brought", "built", "caught", "chosen", "done", "dug", "drawn", "dreamt",
    "driven", "fallen", "felt", "found", "flown", "forgotten", "forgiven", "frozen", "gotten", "given",
    "grown", "hung", "heard", "hidden", "hit", "held", "hurt", "kept", "known", "laid", "led",
    "left", "lent", "let", "lost", "made", "meant", "met", "paid", "put", "read", "ridden",
    "rung", "risen", "run", "said", "seen", "sold", "sent", "set", "shaken", "shone", "shot",
    "sung", "sat", "slept", "spoken", "spent", "stood", "stolen", "swum", "taken", "taught",
    "told", "thought", "thrown", "understood", "woken", "worn", "won", "written", "worked", "talked"
]
# Reglas gramaticales básicas
grammar_rules = {
    "present_simple": {
        "description": "Present simple is used for habitual actions, general truths, and states.",
        "structure": "Subject + base verb (for I, you, we, they) or verb+s/es (for he, she, it)",
        "examples": ["I work.", "She plays soccer."]
    },
    "past_simple": {
        "description": "Past simple is used for actions that happened at a specific time in the past.",
        "structure": "Subject + past form of the verb",
        "examples": ["I worked.", "She played soccer."]
    },
    "past_participle": {
        "description": "Past participles are used for perfect tenses and passive voice.",
        "structure": "Subject + auxiliary verb (have/has/had) + past participle",
        "examples": ["I have worked.", "She has played soccer."]
    },
    "gerund_present_participle": {
        "description": "Gerunds act as nouns, present participles are used for continuous tenses.",
        "structure": "Subject + auxiliary verb + verb+ing",
        "examples": ["I am working.", "She is playing soccer."]
    }
}
