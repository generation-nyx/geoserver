<#global pagetitle=service.title!"GeoServer Features 1.0 Service">
<#global pagepath="/">
<#global pagecrumbs="<b>Home</b>">
<#include "common-header.ftl">
  <div id="breadcrumb" class="py-2 mb-4">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb mb-0">
        <#--  <li class="breadcrumb-item"><a href="#">Home</a></li>
        <li class="breadcrumb-item"><a href="#">Library</a></li>
        <li class="breadcrumb-item active" aria-current="page">Data</li>  -->
      </ol>
    </nav>
  </div>

  <h1>${service.title!"GeoServer Features 1.0 Service"}</h1>
  <p class="my-4">
    ${service.abstract!""}<br/>
    This is the landing page of the Features 1.0 service, providing links to the service API and its contents.<br/>
    This document is also available as
    <#list model.getLinksExcept("landingPage", "text/html") as link><a href="${link.href}">${link.type}</a><#if link_has_next>, </#if></#list>.
  </p>
      
  <div class="row my-3">
    <div class="col-6 col-xl-3">
      <div class="card h-100">
        <div class="card-body">
          <h2>API definition</h2>
          <p>The <a id="htmlApiLink" href="${model.getLinkUrl('api', 'text/html')!}"> API document</a> provides a machine processable description of this service API conformant to OpenAPI 3.
          <br/> 
          This API document is also available as
          <#list model.getLinksExcept("api", "application/json") as link><a href="${link.href}">${link.type}</a><#if link_has_next>, </#if></#list>.
          </p>
        </div>
      </div>
    </div>
    
    <div class="col-6 col-xl-3">
      <div class="card h-100">
        <div class="card-body">
          <h2>Collections</h2>
          <p>The <a id="htmlCollectionsLink" href="${model.getLinkUrl('collections', 'text/html')!}"> collection page</a> provides a list of all the collections available in this service. 
          <br/> 
          This collection page is also available as
          <#list model.getLinksExcept("collections", "text/html") as link><a href="${link.href}">${link.type}</a><#if link_has_next>, </#if></#list>.
          </p>
        </div>
      </div>
    </div>
    <div class="col-6 col-xl-3">
      <div class="card h-100">
        <div class="card-body">
          <#-- TODO when upgrading Freemaker add ?no_esc to avoid html escaping --> 
          ${htmlExtensions('landing')}
        </div>
      </div>
    </div>

    <div class="col-6 col-xl-3">
      <div class="card h-100">
        <div class="card-body">
          <#include "landingpage-conformance.ftl">
        </div>
      </div>
    </div>

  </div>
  <h2>Contact information</h2>
  <address>
    <ul>
      <li>Server managed by ${contact.contactPerson!"-unspecified-"}</li>
      <li>Organization: ${contact.contactOrganization!"-unspecified-"}</li>
      <li>Mail: <a href="mailto:${contact.contactEmail!''}">${contact.contactEmail!"-unspecified-"}</a></li>
    </ul> 
  </address>
<#include "common-footer.ftl">