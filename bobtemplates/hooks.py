from mrbob.bobexceptions import SkipQuestion
from mrbob.bobexceptions import ValidationError


def post_package_name(configurator, question, answer):
    configurator.defaults.update({
        'package.url': 'https://github.com/4teamwork/{}'.format(
            answer),
    })

    try:
        part_1, part_2 = answer.split('.')
    except ValueError:
        raise ValidationError(
            'The format of the packagename have to be e.g.: company.web')

    configurator.variables['package.part_1'] = part_1
    configurator.variables['package.part_1_upper'] = part_1.upper()
    configurator.variables['package.part_1_capitalized'] = part_1.capitalize()

    configurator.variables['package.part_2'] = part_2
    configurator.variables['package.part_2_upper'] = part_2.upper()
    configurator.variables['package.part_2_capitalized'] = part_2.capitalize()

    configurator.variables['package.fullname_underscore'] = "{}_{}".format(
        part_1, part_2)

    configurator.variables['package.fullname_dot'] = "{}.{}".format(
        part_1, part_2)

    configurator.variables['package.fullname_path'] = "{}/{}".format(
        part_1, part_2)

    return answer


def pre_skip_configure_deployment(configurator, question):
    if not configurator.variables['package.configure_deployment']:
        raise(SkipQuestion)


def get_plone_classifier_version(configurator, question, answer):
    an_split = answer.split('.')

    if len(an_split) <= 1:
        raise ValidationError(
            'The plone version needs to have at least 2 digits e.g.: 4.3')

    configurator.variables['package.classifier_version'] = '.'.join(an_split[:2])

    return answer
