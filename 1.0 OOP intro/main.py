import Tv as tv

def main() -> None:
    oTV = tv.TV('Sony', 'Living Room')

    oTV.power()
    oTV.showTVInfo()

    oTV.setChannel(500)
    oTV.power()
    oTV.showTVInfo()

    
if __name__ == "__main__":
    main()