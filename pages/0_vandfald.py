import streamlit as st
import random

st.set_page_config(page_title="Vandfald", page_icon=":droplet:")

st.markdown(
    """
        # Vandfald

        Spillerne trækker på skift et "kort", og følger anvisningerne for kortet. **Træk et kort her :point_down:**
    """
)

cards = [
    "Drik selv 2 slurke",
    "Drik selv 3 slurke",
    "Drik selv 4 slurke",
    "Drik selv 5 slurke",
    "Uddel 2 slurke",
    "Uddel 3 slurke",
    "Uddel 4 slurke",
    "Uddel 5 slurke",
    "Tissekort [1]",
    "Tissekort [2]",
    "Tissekort [3]",
    "Tissekort [4]",
    "Kategori [1]",
    "Kategori [2]",
    "Kategori [3]",
    "Kategori [4]",
    "Heaven [1]",
    "Heaven [2]",
    "Heaven [3]",
    "Heaven [4]",
    "Lav en ny regel [1]",
    "Lav en ny regel [2]",
    "Lav en ny regel [3]",
    "Lav en ny regel [4]",
    "Alle af hankøn skal skåle [1]",
    "Alle af hankøn skal skåle [2]",
    "Alle af hankøn skal skåle [3]",
    "Alle af hankøn skal skåle [4]",
    "Alle af hunkøn skal skåle [1]",
    "Alle af hunkøn skal skåle [2]",
    "Alle af hunkøn skal skåle [3]",
    "Alle af hunkøn skal skåle [4]",
    "Kongen [1]",
    "Kongen [2]",
    "Kongen [3]",
    "Kongen [4]",
    "Vandfald [1]",
    "Vandfald [2]",
    "Vandfald [3]",
    "Vandfald [4]"
]

# Function to get a random card that hasn't been displayed yet
def get_random_card():
    # Retrieve or initialize the displayed cards for the current session
    displayed_cards = st.session_state.get("displayed_cards", [])

    # Check if all cards have been displayed
    if len(displayed_cards) == len(cards):
        return None  # Return None to indicate no more cards

    # Get a random card that hasn't been displayed yet
    card = random.choice([s for s in cards if s not in displayed_cards])

    # Add the card to the set of displayed cards
    displayed_cards.append(card)

    # Update the displayed cards in the session state
    st.session_state.displayed_cards = displayed_cards

    return card

col1, col2, col3 = st.columns(3)

# Button to display a random card
if col2.button("Nyt kort :new:"):
    random_card = get_random_card()

    if random_card is not None:
        st.info(f"{random_card}")
    else:
        st.info("Spillet er slut")


with st.expander("Regler"):
    st.markdown(
        """
            #### REGLERNE:

            1. Alle sidder i en cirkel med en drink eller tre, og en spiller stiller et "mest sandsynligt" spørgsmål. f.eks. "Hvem er mest tilbøjelig til at skade sig selv ved at spille bordtennis?" eller "Hvem er mest tilbøjelig til at komme i problemer med politiet for blotteri?"

            2. På tælling af 3 peger alle på den person, de tror, ville være mest tilbøjelig til at gøre, hvad der blev nævnt.

            3. Du skal tage 1 slurk for hver person, der peger på dig. Så hvis 5 personer tror, at du er mest tilbøjelig til at komme i problemer med politiet for blotteri, skal du tage 5 slurke.

    """
)
