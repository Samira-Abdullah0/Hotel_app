# 🏨 Hotel Management System

A comprehensive Hotel Management module built for Odoo that streamlines hotel operations including customer management, room allocation, and booking processes.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Views](#views)
- [Security](#security)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### 👥 Customer Management
- Complete customer profile management
- Customer identification and contact details
- Gender-based filtering and search capabilities
- Comprehensive customer database

### 🏠 Room Management
- Room number tracking
- Bed capacity management
- Floor-wise room organization
- Easy room allocation system

### 📅 Booking Management
- Booking ID generation and tracking
- Date range management (check-in/check-out)
- Booking history and records
- Seamless reservation process

### 🔐 Security Features
- Role-based access control
- Employee and Manager user groups
- Granular permissions (read, write, create)
- Data security compliance

## 🚀 Installation

### Prerequisites
- Odoo 14.0 or higher
- Python 3.7+
- PostgreSQL database

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/hotel-management-odoo.git
   cd hotel-management-odoo
   ```

2. **Copy to Odoo addons directory**
   ```bash
   cp -r Hotel_app /path/to/odoo/addons/
   ```

3. **Update Odoo addons list**
   - Restart Odoo server
   - Go to Apps menu
   - Click "Update Apps List"

4. **Install the module**
   - Search for "Hotel"
   - Click Install

## 💻 Usage

### Accessing the Module

After installation, navigate to the **Hotel** menu in your Odoo interface. You'll find three main sections:

1. **Customers** - Manage hotel guests and their information
2. **Rooms** - Handle room inventory and specifications
3. **Bookings** - Process reservations and booking records

### Quick Start Guide

1. **Add Customers**: Start by adding customer profiles with their personal details
2. **Configure Rooms**: Set up your hotel rooms with numbers, bed count, and floor information
3. **Create Bookings**: Link customers with rooms and set booking dates

## 🗄️ Models

### Customer Model (`customer.model`)
```python
- customer_name: Char - Customer's full name
- customer_id: Char - Unique customer identifier
- customer_number: Char - Contact phone number
- customer_address: Char - Customer's address
- gender: Selection - Gender (Male/Female)
```

### Room Model (`room.model`)
```python
- room_number: Float - Room identifier number
- beds_number: Float - Number of beds in room
- floor_number: Float - Floor location
```

### Booking Model (`booking.model`)
```python
- booking_id: Float - Unique booking identifier
- date_from: Date - Check-in date
- date_to: Date - Check-out date
```

## 🖼️ Views

### Customer Views
- **Form View**: Detailed customer information entry
- **Tree View**: List view of all customers
- **Search View**: Advanced filtering by name and gender

### Room Views
- **Form View**: Room details and specifications
- **Tree View**: Complete room inventory overview

### Booking Views
- **Form View**: Booking creation and editing
- **Tree View**: All bookings at a glance

## 🔒 Security

The module implements comprehensive security measures:

- **Access Rights**: Configured for all models with appropriate permissions
- **User Groups**: Employee and Manager roles with different access levels
- **Model Access**: Controlled create, read, write, and delete operations
- **Data Integrity**: Prevents unauthorized data deletion

## 📁 Project Structure

```
Hotel_app/
├── models/
│   ├── __init__.py
│   └── hotel.py              # Core business logic
├── views/
│   ├── customer_views.xml    # Customer interface
│   ├── room_views.xml        # Room management interface
│   └── booking_views.xml     # Booking system interface
├── security/
│   ├── ir.model.access.csv   # Access permissions
│   └── security_access.xml   # Security groups and rules
├── static/description/
│   └── icon.png             # Module icon
├── __init__.py
└── __manifest__.py          # Module configuration
```

## 🤝 Contributing

We welcome contributions to improve the Hotel Management System!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow Odoo development best practices
- Write clear, commented code
- Test your changes thoroughly
- Update documentation as needed

## 📋 Requirements

- **Odoo**: Version 14.0+
- **Python**: 3.7 or higher
- **Database**: PostgreSQL
- **Dependencies**: Base Odoo modules

## 🐛 Known Issues

- Currently in active development
- Additional features planned for future releases
- Please report bugs through GitHub issues


## 🏆 Acknowledgments

- Built with ❤️ using Odoo framework
- Thanks to the Odoo community for their excellent documentation
- Special thanks to all contributors and testers
