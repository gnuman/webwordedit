from tastypie.resources import ModelResource
from webwordedit.wordlists.models import Un_Verified_bn_in
from tastypie.authentication import BasicAuthentication
from tastypie.serializers import Serializer
import urlparse
from tastypie.authorization import DjangoAuthorization

class urlencodeSerializer(Serializer):
    formats = ['json', 'jsonp', 'xml', 'yaml', 'html', 'plist', 'urlencode']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'xml': 'application/xml',
        'yaml': 'text/yaml',
        'html': 'text/html',
        'plist': 'application/x-plist',
        'urlencode': 'application/x-www-form-urlencoded',
        }
    def from_urlencode(self, data,options=None):
        """ handles basic formencoded url posts """
        qs = dict((k, v if len(v)>1 else v[0] )
            for k, v in urlparse.parse_qs(data).iteritems())
        return qs

    def to_urlencode(self,content): 
        pass

class Un_Verified_bn_in_resource(ModelResource):
    class Meta:
        serializer = urlencodeSerializer()
        queryset = Un_Verified_bn_in.objects.all()
#        list_allowed_methods = ['get', 'post','put']
        detail_allowed_methods = ['get', 'post', 'put','patch']
        excludes = ['author','time','discard_word','alternate_phrase']
        resource_name = 'un_bn_in'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
