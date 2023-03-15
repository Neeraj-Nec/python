package messageSender

type Sender interface {
	send(number string) bool
}
