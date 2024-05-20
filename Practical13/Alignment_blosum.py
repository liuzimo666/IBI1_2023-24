seq_human = "METTPLNSQKQLSACEDGEDCQENGVLQKVVPTPGDKVESGQISNGYSAVPSPGAGDDTRHSIPATTTTLVAELHQGERETWGKKVDFLLSVIGYAVDLGNVWRFPYICYQNGGGAFLLPYTIMAIFGGIPLFYMELALGQYHRNGCISIWRKICPIFKGIGYAICIIAFYIASYYNTIMAWALYYLISSFTDQLPWTSCKNSWNTGNCTNYFSEDNITWTLHSTSPAEEFYTRHVLQIHRSKGLQDLGGISWQLALCIMLIFTVIYFSIWKGVKTSGKVVWVTATFPYIILSVLLVRGATLPGAWRGVLFYLKPNWQKLLETGVWIDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQDALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHVWAKRRERFVLAVVITCFFGSLVTLTFGGAYVVKLLEEYATGPAVLTVALIEAVAVSWFYGITQFCRDVKEMLGFSPGWFWRICWVAISPLFLLFIICSFLMSPPQLRLFQYNYPYWSIILGYCIGTSSFICIPTYIAYRLIITPGTFKERIIKSITPETPTEIPCGDIRLNAV"
seq_mouse = "METTPLNSQKVLSECKDKEDCQENGVLQKGVPTPADKAGPGQISNGYSAVPSTSAGDEAPHSTPAATTTLVAEIHQGERETWGKKMDFLLSVIGYAVDLGNIWRFPYICYQNGGGAFLLPYTIMAIFGGIPLFYMELALGQYHRNGCISIWKKICPIFKGIGYAICIIAFYIASYYNTIIAWALYYLISSFTDQLPWTSCKNSWNTGNCTNYFAQDNITWTLHSTSPAEEFYLRHVLQIHQSKGLQDLGTISWQLALCIMLIFTIIYFSIWKGVKTSGKVVWVTATFPYIVLSVLLVRGATLPGAWRGVVFYLKPNWQKLLETGVWVDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQDALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHIWAKRREWFVLIVVITCILGSLLTLTSGGAYVVTLLEEYATGPAVLTVALIEAVVVSWFYGITQFCSDVKEMLGFSPGWFWRICWVAISPLFLLFIICSFLMSPPQLRLFQYNYPHWSIILGYCIGTSSVICIPIYIIYRLISTPGTLKERIIKSITPETPTEIPCGDIRMNAV"
seq_rat = "METTPLNSQKVLSECKDREDCQENGVLQKGVPTTADRAEPSQISNGYSAVPSTSAGDEASHSIPAATTTLVAEIRQGERETWGKKMDFLLSVIGYAVDLGNIWRFPYICYQNGGGAFLLPYTIMAIFGGIPLFYMELALGQYHRNGCISIWRKICPIFKGIGYAICIIAFYIASYYNTIIAWALYYLISSLTDRLPWTSCTNSWNTGNCTNYFAQDNITWTLHSTSPAEEFYLRHVLQIHQSKGLQDLGTISWQLTLCIVLIFTVIYFSIWKGVKTSGKVVWVTATFPYIVLSVLLVRGATLPGAWRGVVFYLKPNWQKLLETGVWVDAAAQIFFSLGPGFGVLLAFASYNKFNNNCYQDALVTSVVNCMTSFVSGFVIFTVLGYMAEMRNEDVSEVAKDAGPSLLFITYAEAIANMPASTFFAIIFFLMLITLGLDSTFAGLEGVITAVLDEFPHIWAKRREWFVLIVVITCVLGSLLTLTSGGAYVVTLLEEYATGPAVLTVALIEAVAVSWFYGITQFCSDVKEMLGFSPGWFWRICWVAISPLFLLFIICSFLMSPPQLRLFQYNYPHWSIVLGYCIGMSSVICIPTYIIYRLISTPGTLKERIIKSITPETPTEIPCGDIRMNAV"

# Function to calculate the edit distance between two sequences
def edit_distance(seq1, seq2):
    distance = 0
    # Ensure both sequences are the same length by padding with a dummy character
    # that does not exist in the sequence (e.g., '-').
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    max_len = max(len_seq1, len_seq2)
    seq1 += '-' * (max_len - len_seq1)
    seq2 += '-' * (max_len - len_seq2)
    
    for i in range(max_len):
        if seq1[i] != seq2[i]:
            distance += 1

    return distance

# Function to calculate the percentage identity
def percentage_identity(seq1, seq2, distance):
    identity = (len(seq1) - distance) / len(seq1) * 100
    return identity

# Calculate distances and percentage identities
distance_human_mouse = edit_distance(seq_human, seq_mouse)
percentage_human_mouse = percentage_identity(seq_human, seq_mouse, distance_human_mouse)

distance_human_rat = edit_distance(seq_human, seq_rat)
percentage_human_rat = percentage_identity(seq_human, seq_rat, distance_human_rat)

distance_mouse_rat = edit_distance(seq_mouse, seq_rat)
percentage_mouse_rat = percentage_identity(seq_mouse, seq_rat, distance_mouse_rat)

# Print the results
print(f"Human-Mouse edit distance: {distance_human_mouse}")
print(f"Human-Mouse percentage of identical amino acids: {percentage_human_mouse:.2f}%")
print(f"Human-Rat edit distance: {distance_human_rat}")
print(f"Human-Rat percentage of identical amino acids: {percentage_human_rat:.2f}%")
print(f"Mouse-Rat edit distance: {distance_mouse_rat}")
print(f"Mouse-Rat percentage of identical amino acids: {percentage_mouse_rat:.2f}%")

# Analysis
# Based on the percentage identity, determine which species is more closely related to human
if percentage_human_mouse > percentage_human_rat:
    print("The human SLC6A4 gene sequence is more similar to the mouse.")
else:
    print("The human SLC6A4 gene sequence is more similar to the rat.")

# Suggest which rodent species would be a better model organism for studying human SLC6A4 gene variation
if percentage_human_mouse > percentage_human_rat:
    print("The mouse may be a better model organism for studying variation in the human SLC6A4 gene.") 
else:
    print("The rat may be a better model organism for studying variation in the human SLC6A4 gene.")