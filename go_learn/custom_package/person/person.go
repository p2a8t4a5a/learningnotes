package person


func Description(name string) string {
    return "the Person name is: " + name
}

func secretName(name string) string {
    """ this is private """
    return "Do not share"
}
