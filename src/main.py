"""
Main entry point for Invisibility Cloak project
Run this file to start the application
"""

from cloak import InvisibilityCloak
from utils import print_welcome_message

def main():
    """Main function to run the invisibility cloak"""
    # Print welcome message
    print_welcome_message()
    
    # Create and run the invisibility cloak
    try:
        cloak = InvisibilityCloak()
        cloak.run()
    except KeyboardInterrupt:
        print("\n⚠️  Program interrupted by user")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
    finally:
        print("\n👋 Thank you for using Invisibility Cloak!")

if __name__ == "__main__":
    main()