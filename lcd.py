import board
import busio
import adafruit_character_lcd.character_lcd_i2c as characterlcd

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# LCD size (e.g., 16x2 or 20x4)
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD over I2C
lcd = characterlcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

# Clear the LCD and display a message
lcd.clear()
lcd.message = "Hello, I2C World!"

# Optionally, you can also control the backlight
lcd.backlight = True  # Turn on backlight
