# Financial Atlas 📊

> **Your Complete Map to Financial Independence and Smart Investing**

A comprehensive single-page HTML application for retirement planning, FIRE calculations, portfolio management, and live market data analysis. Built with React, Chart.js, and modern financial APIs to help you navigate your path to financial freedom.

![Financial Atlas Demo](https://img.shields.io/badge/Status-Live-brightgreen) ![License](https://img.shields.io/badge/License-MIT-blue) ![Version](https://img.shields.io/badge/Version-2.0-orange)

## 🚀 Features

### 💰 Financial Planning Tools
- **FIRE Calculator**: Calculate your Financial Independence Retire Early timeline
- **Compound Interest Calculator**: Visualize long-term investment growth
- **Monte Carlo Simulation**: Risk analysis with configurable scenarios
- **Retirement Planner**: Comprehensive retirement timeline projections

### 📈 Live Market Data
- **Real-time Stock Quotes**: Powered by Yahoo Finance API
- **Market Indices Tracking**: S&P 500, NASDAQ, Dow Jones, Russell 2000, VIX
- **ETF & Stock Analysis**: Popular ETFs and individual stock performance
- **Interactive Charts**: Mini price history charts with trend analysis
- **Market Heat Map**: Visual representation of market performance
- **Custom Watchlists**: Search and track your favorite securities

### 🎯 Investment Guidance
- **Lazy Portfolio Strategies**: Pre-built portfolio allocations
- **Educational Guides**: Comprehensive guides on FIRE, investing, and market basics
- **Risk Analysis**: Portfolio volatility and risk assessment tools
- **Currency Support**: Multi-currency calculations (USD, EUR, GBP, CAD, AUD, etc.)

### 🔧 Advanced Features
- **Session Analytics**: Track your usage and calculations
- **Keyboard Shortcuts**: Power user navigation
- **Data Persistence**: Local storage for settings and preferences
- **Responsive Design**: Optimized for desktop, tablet, and mobile
- **Dark/Light Themes**: Automatic theme detection
- **Toast Notifications**: Real-time feedback and status updates

## 🛠️ Technology Stack

- **Frontend**: React 18, HTML5, CSS3, JavaScript ES6+
- **Styling**: Tailwind CSS, Custom CSS Variables
- **Charts**: Chart.js 4.4.0
- **Icons**: Font Awesome 6.5.0
- **Animations**: Framer Motion 11.0.0
- **Financial Data**: Yahoo Finance API, FX Rates API
- **Math**: Math.js, Money.js for currency conversion

## 📦 Installation & Setup

### Option 1: Direct Usage (Recommended)
Simply download and open `index.html` in any modern web browser. No installation required!

```bash
# Clone the repository
git clone https://github.com/drakeaxelrod/financial-atlas.git
cd financial-atlas

# Open in browser
open index.html
# or
python -m http.server 8000  # For local server
```

### Option 2: Local Development Server
```bash
# Using Python
python -m http.server 8000

# Using Node.js (if you have it)
npx serve .

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

## 🎮 Usage Guide

### Quick Start
1. **Open the app** in your web browser
2. **Navigate tabs** using the top navigation or keyboard shortcuts (Ctrl+1, Ctrl+2, etc.)
3. **Configure your financial parameters** in the input fields
4. **View real-time calculations** and projections
5. **Explore market data** with live quotes and analysis

### Dashboard Overview
- **FIRE Number**: Your target amount for financial independence
- **Years to FIRE**: Timeline based on current savings rate
- **Projected Savings**: Total estimated savings at retirement
- **Market Snapshot**: Quick view of major market indices

### Calculator Features
- **Compound Interest**: Visualize investment growth over time
- **FIRE Planning**: Calculate your path to financial independence
- **Monte Carlo**: Run risk simulations with customizable parameters
- **Market Data**: Real-time tracking of stocks, ETFs, and indices

### Keyboard Shortcuts
- `Ctrl/Cmd + 1`: Dashboard
- `Ctrl/Cmd + 2`: Market Data
- `Ctrl/Cmd + 3`: Guides
- `Ctrl/Cmd + 4`: Monte Carlo
- `Ctrl/Cmd + R`: Refresh market data (when in Market Data tab)

## 📊 Supported Markets & Currencies

### Currencies
- 🇺🇸 US Dollar (USD)
- 🇪🇺 Euro (EUR)
- 🇬🇧 British Pound (GBP)
- 🇨🇦 Canadian Dollar (CAD)
- 🇦🇺 Australian Dollar (AUD)
- 🇸🇪 Swedish Krona (SEK)
- 🇳🇴 Norwegian Krone (NOK)
- 🇩🇰 Danish Krone (DKK)
- 🇨🇭 Swiss Franc (CHF)
- 🇯🇵 Japanese Yen (JPY)

### Market Data Sources
- **Primary**: Yahoo Finance API (real-time quotes)
- **Fallback**: Cached data with graceful degradation
- **Update Frequency**: 1-minute intervals for live data
- **Cache Duration**: 5 minutes for optimal performance

## 🔧 Configuration

### Default Settings
```javascript
{
  currentAge: 30,
  retirementAge: 65,
  currentSavings: 50000,
  monthlySavings: 2000,
  annualReturn: 7,
  monthlyExpenses: 4000,
  safeWithdrawalRate: 4,
  inflationRate: 2.5,
  currency: 'USD',
  volatility: 15,
  numSimulations: 1000
}
```

### Customization
All settings are automatically saved to local storage and persist between sessions. You can:
- Adjust financial parameters in real-time
- Switch currencies with automatic conversion
- Customize market data refresh intervals
- Set up custom stock watchlists

## 🚨 Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ❌ Internet Explorer (not supported)

## 🔒 Privacy & Data

- **No server required**: Runs entirely in your browser
- **Local data storage**: All settings saved locally
- **No tracking**: No analytics or user tracking
- **API calls**: Only to public financial APIs (Yahoo Finance, FX Rates)
- **Offline capable**: Cached data available when offline

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines

- Keep the single-file architecture
- Follow existing code style and patterns
- Test on multiple browsers
- Update documentation for new features
- Ensure responsive design compatibility


## 🐛 Troubleshooting

### Common Issues

**Market data not loading?**
- Check internet connection
- Verify browser allows API requests
- Try refreshing the page
- Check browser console for errors

**Calculations seem wrong?**
- Verify all input parameters
- Check currency settings
- Ensure realistic values (avoid negative numbers)
- Reset to defaults if needed

**Performance issues?**
- Disable auto-refresh in market data
- Clear browser cache
- Close other browser tabs
- Use latest browser version

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Yahoo Finance** for market data API
- **FX Rates API** for currency conversion
- **Chart.js** for beautiful charting capabilities
- **React Team** for the amazing framework
- **Tailwind CSS** for utility-first styling
- **Font Awesome** for comprehensive iconography

## 📞 Support

- 📧 **Email**: [drakeaxelrod@gmail.com]
- 🐛 **Issues**: [GitHub Issues](https://github.com/drakeaxelrod/financial-atlas/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/drakeaxelrod/financial-atlas/discussions)
- 📖 **Wiki**: [Project Wiki](https://github.com/drakeaxelrod/financial-atlas/wiki)

---

**Built with ❤️ for the Financial Independence community**

*Disclaimer: This tool is for educational and planning purposes only. Always consult with qualified financial advisors before making investment decisions.*
