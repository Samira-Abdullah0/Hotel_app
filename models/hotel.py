from odoo import models,fields


class HotelManagement(models.Model):
    _name = 'customer.model'
    _description = 'Hotel management'

    customer_name = fields.Char(string='customer name')
    customer_id = fields.Char(string='customer id')
    customer_number = fields.Char(string='customer number')
    customer_address = fields.Char(string=' customer address')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], 'gender')

class RoomManagement(models.Model):
    _name = 'room.model'
    _description = 'Room management'

    room_number = fields.Float(string='room number')
    beds_number = fields.Float(string='beds number')
    floor_number = fields.Float(string='floor number')


class Booking (models.Model):
    _name = 'booking.model'
    _description = 'Booking management'

    booking_id = fields.Float(string='booking id')
    date_from = fields.Date(string='date from')
    date_to = fields.Date(string='date to')