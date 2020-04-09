

# my_lambdata/polos.py

class Polo():
    def __init__(self, color, size, price=99.00, style=None):
        self.color = color
        self.size = size
        self.price = price
        self.style = style

if __name__ == "__main__":

    #df = DataFrame(...)
    # df.head()
    polo1 = Polo(color="Blue", size="L", price=4.99)
    print(polo1.color)
    print(polo1.price)

    polo2 = Polo(color="Yellow", size="Small")
    print(polo2.color)
    print(polo2.price)
