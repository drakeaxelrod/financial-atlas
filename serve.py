#!/usr/bin/env python
"""
Simple HTTP server script for hosting and debugging the Financial Atlas HTML file.
This script provides a local development server with automatic reloading and CORS support.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import argparse
from pathlib import Path
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with CORS support for API calls."""

    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_OPTIONS(self):
        """Handle preflight requests."""
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        """Custom logging with timestamps."""
        timestamp = time.strftime('[%Y-%m-%d %H:%M:%S]')
        print(f"{timestamp} {format % args}")

class FileChangeHandler(FileSystemEventHandler):
    """Handler for file system events to trigger browser reload."""

    def __init__(self, callback):
        self.callback = callback
        self.last_modified = {}

    def on_modified(self, event):
        if event.is_directory:
            return

        # Only watch HTML, CSS, JS files
        if event.src_path.endswith(('.html', '.css', '.js')):
            # Debounce rapid file changes
            now = time.time()
            if event.src_path not in self.last_modified or now - self.last_modified[event.src_path] > 1:
                self.last_modified[event.src_path] = now
                self.callback(event.src_path)

def start_file_watcher(directory, callback):
    """Start watching files for changes."""
    event_handler = FileChangeHandler(callback)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    return observer

def on_file_changed(file_path):
    """Callback when a file is changed."""
    print(f"📁 File changed: {os.path.basename(file_path)}")
    print("🔄 Refresh your browser to see changes")

def check_dependencies():
    """Check if required files exist."""
    required_files = ['index.html']
    missing_files = []

    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False

    return True

def get_network_ip():
    """Get the local network IP address."""
    import socket
    try:
        # Connect to a remote server to get local IP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            return s.getsockname()[0]
    except Exception:
        return '127.0.0.1'

def main():
    parser = argparse.ArgumentParser(
        description='Local development server for Financial Atlas',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python serve.py                    # Start server on default port 8000
  python serve.py -p 3000           # Start server on port 3000
  python serve.py --no-browser      # Start server without opening browser
  python serve.py --no-watch        # Start server without file watching
        """
    )

    parser.add_argument(
        '-p', '--port',
        type=int,
        default=8000,
        help='Port to serve on (default: 8000)'
    )

    parser.add_argument(
        '--no-browser',
        action='store_true',
        help='Don\'t automatically open browser'
    )

    parser.add_argument(
        '--no-watch',
        action='store_true',
        help='Don\'t watch files for changes'
    )

    parser.add_argument(
        '--host',
        default='127.0.0.1',
        help='Host to bind to (default: 127.0.0.1, use 0.0.0.0 for all interfaces)'
    )

    args = parser.parse_args()

    # Change to the directory containing this script
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    # Check if required files exist
    if not check_dependencies():
        sys.exit(1)

    # Start file watcher if enabled
    observer = None
    if not args.no_watch:
        try:
            observer = start_file_watcher('.', on_file_changed)
            print("👀 File watcher started - changes will be detected")
        except ImportError:
            print("⚠️  File watching not available (install watchdog: pip install watchdog)")
        except Exception as e:
            print(f"⚠️  Could not start file watcher: {e}")

    # Create and configure the server
    handler = CORSHTTPRequestHandler

    try:
        with socketserver.TCPServer((args.host, args.port), handler) as httpd:
            host_display = args.host if args.host != '0.0.0.0' else get_network_ip()

            print("\n" + "="*60)
            print("🚀 Financial Atlas Development Server")
            print("="*60)
            print(f"📁 Serving directory: {os.getcwd()}")
            print(f"🌐 Local URL:        http://127.0.0.1:{args.port}")

            if args.host == '0.0.0.0':
                network_ip = get_network_ip()
                print(f"🌍 Network URL:      http://{network_ip}:{args.port}")

            print(f"📝 Main file:        index.html")
            print("="*60)
            print("💡 Tips:")
            print("   • Press Ctrl+C to stop the server")
            print("   • Refresh browser to see changes")
            if not args.no_watch:
                print("   • File changes are automatically detected")
            print("   • Check browser console for any errors")
            print("="*60)

            # Open browser if requested
            if not args.no_browser:
                url = f"http://127.0.0.1:{args.port}"
                print(f"🔗 Opening browser: {url}")
                threading.Timer(1, lambda: webbrowser.open(url)).start()

            print(f"\n✅ Server running on http://{host_display}:{args.port}")
            print("   Press Ctrl+C to stop\n")

            # Start serving
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {args.port} is already in use. Try a different port:")
            print(f"   python serve.py -p {args.port + 1}")
        else:
            print(f"❌ Server error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)
    finally:
        if observer:
            observer.stop()
            observer.join()

if __name__ == '__main__':
    main()
