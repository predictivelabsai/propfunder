# Acknowledgements

## Original Project

This project is based on and refactored from the **Landex Backend** - a land crowdfunding platform.

**Original Repository**: https://github.com/kaljuvee/landex-backend.git

### Original Authors

- **Kaljuvee** - Original developer and maintainer
- **Predictive Labs AI Team** - Original project team

## Refactoring and Adaptation

The Litfunder Backend represents a comprehensive refactoring and domain adaptation of the original Landex platform:

### Key Changes

1. **Domain Transformation**: Land Crowdfunding → Litigation Finance
2. **Model Refactoring**: 
   - Land → LegalCase
   - Crowdfund → CaseFunding
   - InvestCrowdfund → CaseInvestment
   - Added litigation-specific models (Settlement, CaseVoting, etc.)

3. **Dependency Upgrades**: All packages updated to latest versions
4. **Service Migration**: Sendgrid → Postmark for email
5. **Database**: PostgreSQL integration with new schema
6. **Testing**: Comprehensive test suite with mock data generation
7. **Documentation**: Complete documentation and deployment guides

## Contributors

**Refactoring Team**: Litfunder Development Team (2025)

## Technologies Used

### Core Framework
- Django 5.2.8 - Web framework
- Python 3.11 - Programming language
- PostgreSQL - Database

### Services
- Postmark - Email service
- Twilio - SMS service
- Firebase - Push notifications (optional)

### Development Tools
- Git - Version control
- pytest - Testing framework
- Coverage.py - Code coverage

## License

This project maintains the same license as the original Landex project.

## Special Thanks

- Original Landex team for the solid foundation
- Django community for excellent documentation
- All contributors and testers

## Citation

If you use this project, please cite:

```
Litfunder Backend - Litigation Finance Platform
Refactored from Landex Backend
https://github.com/predictivelabsai/litfunder-backend
```

---

**Refactoring Date**: November 28, 2025  
**Status**: Production Ready v1.0.0
